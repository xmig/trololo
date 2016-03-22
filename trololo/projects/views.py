from serializers import TaskSerializer
from rest_framework.generics import GenericAPIView
from projects.models import Task
from models import Project
from serializers import ProjectSerializer
from rest_framework import generics
from django_filters import FilterSet, NumberFilter, CharFilter, IsoDateTimeFilter
from rest_framework import filters



class TaskData(GenericAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request):

        return Response(
            TaskSerializer(self.get_queryset(), many=True).data
        )


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users:user_list', request=request),
        'projects': reverse('projects:projects', request=request),
        'tasks': reverse('projects:tasks', request=request)
    })


class ProjectFilter(FilterSet):
    user = NumberFilter(name='member__id', lookup_expr='exact')
    name = CharFilter(name='name', lookup_expr='iexact')
    id = NumberFilter(name='id',lookup_expr='exact')
    content_description = CharFilter(name='description', lookup_type='icontains')

    date_to_started = NumberFilter(name='date_started', lookup_expr='day')
    date_to_started_gt = IsoDateTimeFilter(name='date_started',lookup_expr='gte')
    date_to_started_lt = IsoDateTimeFilter(name='date_started',lookup_expr='lte')

    class Meta:
        model = Project
        fields = [
            'name', 'status', 'description', 'id', 'content_description', 'date_to_started',
            'date_to_started_gt', 'date_to_started_lt', 'user'
        ]


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = ProjectFilter
    search_fields = ('name', 'description', 'id')
    ordering_fields = ('name', 'id', 'description', 'date_started')


