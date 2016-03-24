from serializers import ProjectSerializer, TaskSerializer
from rest_framework import status
from projects.models import Project, Task

from rest_framework import filters
from rest_framework import generics
from django_filters import FilterSet, NumberFilter, CharFilter, IsoDateTimeFilter

from django.http import Http404

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


class ProjectsList(generics.ListCreateAPIView):
    """
    Get/Update data.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = ProjectFilter
    search_fields = ('name', 'description', 'id')
    ordering_fields = ('name', 'id', 'description', 'date_started')


    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProjectDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Project instance.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class TaskList(generics.GenericAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Task instance.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
