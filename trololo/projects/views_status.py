from serializers import StatusSerializer
from rest_framework import status
from projects.models import Status
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response

from rest_framework import filters
from django_filters import FilterSet, NumberFilter, CharFilter


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


class StatusView(generics.ListCreateAPIView):
    """
    Method get returns a list of statuses
    Method post creates new status
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = StatusFilter
    search_fields = ('name', )
    ordering_fields = ('name', 'order_number', 'project')


class StatusDetail(generics.GenericAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_object(self, pk):
        try:
            return Status.objects.get(pk=pk)
        except Status.DoesNotExist:
            raise Http404

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
        serializer = StatusSerializer(stat, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        This method delete status
        """
        st = self.get_object(pk)
        st.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

