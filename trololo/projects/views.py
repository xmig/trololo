from serializers import ProjectSerializer, TaskSerializer
from rest_framework import status
from projects.models import Project, Task
from django.db.models import Q

from rest_framework import filters
from rest_framework import generics
from django_filters import FilterSet, NumberFilter, CharFilter, IsoDateTimeFilter

from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from activity.serializers import ActivitySerializer
from activity.filters import ActivityFilter
from activity.models import Activity


@api_view(['GET'])
def api_root(request, format=None):
    """
    Return api root
    """
    return Response({
        'users': reverse('users:user_list', request=request),
        'projects': reverse('projects:projects', request=request),
        'tasks': reverse('tasks:tasks', request=request),
        'status': reverse('statuses:status', request=request)
    })


class ProjectFilter(FilterSet):
    """
    Project filter
    """
    user = NumberFilter(name='member__id', lookup_expr='exact')
    name = CharFilter(name='name', lookup_expr='iexact')
    id = NumberFilter(name='id',lookup_expr='exact')
    description = CharFilter(name='description', lookup_type='icontains')

    date_to_started = NumberFilter(name='date_started', lookup_expr='day')
    date_to_started_gt = IsoDateTimeFilter(name='date_started',lookup_expr='gte')
    date_to_started_lt = IsoDateTimeFilter(name='date_started',lookup_expr='lte')

    class Meta:
        model = Project
        fields = [
            'name', 'status', 'description', 'id', 'date_to_started',
            'date_to_started_gt', 'date_to_started_lt', 'user'
        ]


class ProjectsList(generics.ListCreateAPIView):
    """
    Get/Update data.
    """
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = ProjectFilter
    search_fields = ('name', 'description', 'id')
    ordering_fields = ('name', 'id', 'description', 'date_started')

    def get_queryset(self):
        current_user = self.request.user
        # if current_user.is_superuser:
        #     return Project.objects.all()
        # else:
        return Project.objects.filter(Q(members=current_user) | Q(created_by=current_user))

    def post(self, request):
        serializer = ProjectSerializer(data=request.data, context={'request': request})

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
        serializer = ProjectSerializer(project, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectTaskFilter(FilterSet):
    """
    Project task filetr
    """
    name = CharFilter(name='name', lookup_expr='iexact')
    description = CharFilter(name='description', lookup_type='icontains')
    status = CharFilter(name='status', lookup_expr='icontains')
    type = CharFilter(name='type', lookup_expr='icontains')
    label = CharFilter(name='label', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = [
            'name', 'description',
            'status', 'type', 'label'
        ]



class TaskList(generics.ListCreateAPIView):
    """
    Return filtering tasks
    """
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ProjectTaskFilter
    search_fields = ('name', 'description', 'status', 'type', 'label')
    ordering_fields = ('name', 'description', 'status', 'type', 'label')

    def get_queryset(self):
        current_user = self.request.user
        # if current_user.is_superuser:
        #     return Task.objects.all()
        # else:
        return Task.objects.filter(Q(project__members=current_user) | Q(project__created_by=current_user))

    def post(self, request):
        serializer = TaskSerializer(data=request.data, context={'request': request})

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
        serializer = TaskSerializer(task, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectActivity(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_class = ActivityFilter
    # ordering_fields = '__all__'
    ordering_fields = ('message', 'created_at',)
    ordering = ('-created_at',)

    def get(self, request, id, show_type):
        """
        Get project activity data by project id \n
        Activity ordering by created_at DESC \n\n
        {id} - project_id \n
        {show_type}  : \n
        a  -  get all activity \n
        p  - get only project activity \n
        t  - get only task activity \n\n

        Available filters:\n
        for_cu        - get data filtered by current user\n
        message       - filter by strict activity message\n
        message_like  - filter by contains activity message (insensitive)\n
        date_0        - from date (created_at)\n
        date_1        - to date (created_at)\n\n

        Available sorting (send param like this ?sorting=filter1,filter2,.....):\n

        message\n
        -message\n
        created_at\n
        -created_at\n

        """
        try:
            for_current_user=request.GET.get('for_cu', False)
            self.queryset = self.filter_queryset(self.get_queryset())

            if show_type == 'a':
                # all activity
                activity_type_query = Q(project_activities=int(id)) | Q(task_activities__project__id=int(id))
            elif show_type == 'p':
                # project only activity
                activity_type_query = Q(project_activities=int(id))
            elif show_type == 't':
                # task only activity
                activity_type_query = Q(task_activities__project__id=int(id))
            else:
                activity_type_query = Q(project_activities=int(id)) | Q(task_activities__project__id=int(id))

            activities = self.get_queryset().filter(activity_type_query)

            if for_current_user:
                activities = activities.filter(created_by=int(request.user.id))

            data = ActivitySerializer(activities, many=True).data
            response = Response(data)
        except Project.DoesNotExist:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
