from serializers import ProjectSerializer, TaskSerializer # ProjectCommentSerializer, TaskCommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from projects.models import Project, Task
from models import Project
from serializers import ProjectSerializer
from rest_framework import generics
import django_filters
from rest_framework import filters



# class ProjectData(GenericAPIView):
#     serializer_class = ProjectSerializer
#     queryset = Project.objects.all()
#
#     def get(self, request):
#
#         return Response(
#             ProjectSerializer(self.get_queryset(), many=True).data
#         )

    # def put(self,request):
    #     s = self.get_serializer_class()(request.project, data=request.data)
    #
    #     if s.is_valid():
    #         s.save()
    #
    #         return Response(s.data, status=status.HTTP_201_CREATED)
    #     return Response({"errors": s.errors}, status=status.HTTP_400_BAD_REQUEST)


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


class ProjectFilter(django_filters.FilterSet):
    name_project = django_filters.CharFilter(name='name', lookup_expr='iexat')
    id_project = django_filters.NumberFilter(name='id',lookup_expr='exact')
    content_description = django_filters.CharFilter(name='description', lookup_type='icontains')

    date_to_started = django_filters.IsoDateTimeFilter(name='date_started', lookup_expr='day')
    date_to_started_gt = django_filters.IsoDateTimeFilter(name='date_started',lookup_expr='gte')
    date_to_started_lt = django_filters.IsoDateTimeFilter(name='date_started',lookup_expr='lte')

    class Meta:
        model = Project
        fields = [
            'name', 'status', 'description', 'id_project', 'content_description', 'date_to_started',
            'date_to_started_gt', 'date_to_started_lt'
        ]


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = ProjectFilter
    search_fields = ('name', 'description', 'id_project')
    ordering_fields = ('name', 'id', 'description', 'date_started')

