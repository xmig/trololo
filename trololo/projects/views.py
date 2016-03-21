from serializers import ProjectSerializer, TaskSerializer # ProjectCommentSerializer, TaskCommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from projects.models import Project, Task



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
        # 'users': reverse('users', request=request, format=format),
        'projects': reverse('projects:projects', request=request, format=format),
        'tasks': reverse('projects:tasks', request=request, format=format)
    })

from rest_framework import viewsets
from models import Project
from serializers import ProjectSerializer
from rest_framework import generics
import django_filters
from rest_framework import filters


class ProjectFilter(django_filters.FilterSet):
    name_project = django_filters.CharFilter(name='name', lookup_expr='iexat')
    id_project = django_filters.NumberFilter(name='id',lookup_expr='exact')
    content_description = django_filters.CharFilter(name='description', lookup_type='icontains')

    date_to_started = django_filters.IsoDateTimeFilter(name='date_started', lookup_expr='day')
    date_to_started_gt = django_filters.IsoDateTimeFilter(name='date_started',lookup_expr='gte')
    date_to_started_lt = django_filters.IsoDateTimeFilter(name='date_started',lookup_expr='lte')

    class Meta:
        model = Project
        fields = ['name', 'status', 'description', 'id_project', 'content_description', 'date_to_started', 'date_to_started_gt', 'date_to_started_lt']


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProjectFilter


# class ProjectData(generics.RetrieveAPIView):
#     serializer_class = ProjectSerializer
#     lookup_field = 'id'
#     queryset = Project.objects.all()

#
# class ProjectData(generics.ListAPIView):
#     serializer_class = ProjectSerializer
#
#     def get_queryset(self):
#         projectname = self.kwargs['name']
#         # projectdescription = self.kwargs['description']
#
#         # return Project.objects.filter( description=projectdescription)
#         return Project.objects.filter(name=projectname)

# 111111
class ProjectData(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):

        queryset = Project.objects.all()
        # projectname = self.request.query_params.get('projectname', None)
        # if projectname is not None:
        params = {k: v for k, v in self.request.query_params.items()}
        queryset = queryset.filter(**params)
        return queryset


# class ProjectData(generics.GenericAPIView):
#     serializer_class = ProjectSerializer
#
#     def get(self):
#         return Response(
#             ProjectSerializer(self.get_queryset(), nane="name")
#         )

    # def get_queryset(self):
    #     project_id = self.kwargs['id']
    #     # queryset = self.Project
    #
    #     return Project.objects.get(id=project_id)
        # return Response(
        #     ProjectSerializer(self.get_queryset(), many=True).data
        # )