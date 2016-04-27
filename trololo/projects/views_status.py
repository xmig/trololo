from serializers import StatusSerializer
from rest_framework import status
from projects.models import Status, Project
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response

from rest_framework import filters
from django_filters import FilterSet, NumberFilter, CharFilter
from django.db.models import Q
from rest_framework import exceptions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_extensions.cache.decorators import cache_response


class StatusFilter(FilterSet):
    """
    Status filtering
    """

    name = CharFilter(name='name', lookup_expr='iexact')
    number = NumberFilter(name='order_namber')
    project = NumberFilter(name='project__id')

    class Meta:
        model = Status
        fields = ['name', 'number', 'project']


import json
from django.core.cache import caches


class StatusView(generics.ListCreateAPIView):
    """
    Method get returns a list of statuses
    Method post creates new status
    """
    serializer_class = StatusSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = StatusFilter
    search_fields = ('name', )
    ordering_fields = ('name', 'order_number', 'project')
    pagination_class = LimitOffsetPagination

    def _get_last_order_number(self, project):
        last_status = Status.objects.filter(project=project) \
            .order_by('-order_number').first()

        return last_status.order_number if last_status else 0

    @cache_response(60 * 15, key_func='calculate_cache_key')
    def get(self, request, *args, **kwargs):
        print "In status view!!!"
        return self.list(request, *args, **kwargs)

    # TODO: move this to the separate function
    def calculate_cache_key(self, view_instance, view_method, request, args, kwargs):

        key = '::'.join([
            view_instance.__class__.__name__,
            view_method.__name__,
            json.dumps(dict(request.query_params)).replace(' ', ''),
            request.user.username
        ])

        return key

    def get_queryset(self):
        user = self.request.user
        proj = [
            pr.id for pr in Project.objects.filter(Q(members=user) | Q(created_by=user)).all()
        ]
        return Status.objects.filter(project__id__in=proj)

    def post(self, request):
        serializer = StatusSerializer(data=request.data, context={'request': request}, partial=True)

        user = self.request.user
        proj = [
            pr.id for pr in Project.objects.filter(Q(members=user) | Q(created_by=user)).all()
        ]

        if serializer.is_valid():

            project = serializer.validated_data['project'].id
            order_number = serializer.validated_data.get(
                'order_number', self._get_last_order_number(project) + 1
            )
            serializer.validated_data['order_number'] = order_number

            stat = Status.objects.filter(
                project=serializer.validated_data['project'],
                order_number__gte=order_number
            ).order_by('order_number').all()

            if project not in proj:
                return Response(
                    {'detail':"You don't have access permissions for project with id {}".format(project)},
                    status.HTTP_403_FORBIDDEN
                )
            elif stat:
                if stat[0].order_number == order_number:
                    for item in stat:
                        item.order_number += 1
                        item.save()

            serializer.save()

            # clear cache, experimental
            # TODO: create decorator that checks Response status code and clears cache for all 2XX statuses
            c = caches['default']
            keys = c.keys("{0}*".format(self.__class__.__name__))
            for key in keys:
                c.delete(key)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class StatusDetail(generics.GenericAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_object(self, pk):
        try:
            status = Status.objects.select_related("project").get(pk=pk)
        except Status.DoesNotExist:
            raise exceptions.NotFound(
                detail="Status with id {} does not exist.".format(pk)
            )

        user = self.request.user

        if status.project.created_by != user and user not in status.project.members.all():
            raise exceptions.PermissionDenied(
                detail="You don't have access permissions for status with id {}".format(pk)
            )
        return status

    def get(self, request, pk):
        """
        This method returns the status by id
        """
        status = self.get_object(pk)
        serializer = StatusSerializer(status, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        """
       This method rename status
        """
        stat = self.get_object(pk)
        serializer = StatusSerializer(stat, data=request.data, context={'request': request}, partial=True)
        user = self.request.user
        proj = [
            pr.id for pr in Project.objects.filter(Q(members=user) | Q(created_by=user)).all()
        ]
        if serializer.is_valid():
            project = serializer.validated_data['project'].id
            order_number = serializer.validated_data['order_number']

            stat = Status.objects.filter(
                project=serializer.validated_data['project'],
                order_number__gte=order_number
            ).order_by('order_number').all()

            if project not in proj:
                return Response(
                    {'detail':"You don't have access permissions for project with id {}".format(project)},
                    status.HTTP_403_FORBIDDEN
                )
            elif stat:
                if stat[0].order_number == order_number:
                    for item in stat:
                        item.order_number += 1
                        item.save()
            serializer.save()

            return Response(serializer.data)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        This method delete status
        """
        st = self.get_object(pk)
        st.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

