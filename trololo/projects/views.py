import requests
from django.conf import settings
from logging import getLogger

from serializers import (
    ProjectSerializer, TaskSerializer, TaskCreateSerializer, ProjectCommentSerializer,
    TaskCommentSerializer, TagSerializer, UploadFileSerializer
)
from rest_framework import status
from projects.models import Project, Task, ProjectComment, TaskComment, TaskPicture
from django.db.models import Q

from rest_framework import filters
from rest_framework import generics
from django_filters import FilterSet, NumberFilter, CharFilter, IsoDateTimeFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import exceptions

from chi_django_base.paginators import StandardResultsSetPagination
from chi_django_base.sphinx_perform_search import perform_search

from activity.serializers import ActivitySerializer
from activity.filters import ActivityFilter
from activity.models import Activity
from django.conf import settings


_logger = getLogger('app')


def get_my_proj(me):
    proj = [
        pr.id for pr in Project.objects.filter(Q(members=me) | Q(created_by=me))
    ]

    return proj


@api_view(['GET'])
def api_root(request, format=None):
    """
    Return api root
    """
    return Response({
        'users': reverse('users:user_list', request=request),
        'projects': reverse('projects:projects', request=request),
        'tasks': reverse('tasks:tasks', request=request),
        'status': reverse('statuses:status', request=request),
        'comments_projects': reverse('comments_projects:comments', request=request),
        'comments_tasks': reverse('comments_tasks:comments', request=request),

    })


class ProjectFilter(FilterSet):
    """
    Project filter
    """
    user = NumberFilter(name='member__id', lookup_expr='exact')
    name = CharFilter(name='name', lookup_expr='iexact')
    id = NumberFilter(name='id',lookup_expr='exact')
    description = CharFilter(name='description', lookup_type='icontains')
    tag = CharFilter(name='tags__name')

    date_to_started = NumberFilter(name='date_started', lookup_expr='day')
    date_to_started_gt = IsoDateTimeFilter(name='date_started',lookup_expr='gte')
    date_to_started_lt = IsoDateTimeFilter(name='date_started',lookup_expr='lte')

    class Meta:
        model = Project
        fields = [
            'name', 'status', 'description', 'id', 'date_to_started',
            'date_to_started_gt', 'date_to_started_lt', 'user', 'tag'
        ]


class ProjectsList(generics.ListCreateAPIView):
    """
    Get/Update data.
    """
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = ProjectFilter
    search_fields = ('name', 'description', 'id', 'tags__name')
    ordering_fields = ('name', 'id', 'description', 'date_started')

    def get_queryset(self):
        return Project.objects.filter(id__in=get_my_proj(self.request.user))

    def post(self, request):
        serializer = ProjectSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class ProjectDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Project instance.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise exceptions.NotFound(
                detail="Project with id {} does not exist.".format(pk)
            )
        user = self.request.user
        if project.created_by != user and user not in project.members.all():
            raise exceptions.PermissionDenied(
                detail="You don't have access permissions for project with id {}".format(pk)
            )
        return project

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
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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
    tag = CharFilter(name='tags__name')
    group = NumberFilter(name='group', lookup_expr='exact')
    member = NumberFilter(name='members', lookup_expr='exact')

    class Meta:
        model = Task
        fields = [
            'name', 'description', 'status', 'type', 'label', 'project', 'group', 'tag', 'member'
        ]


class TaskList(generics.ListCreateAPIView):
    """
    Return filtering tasks
    """
    serializer_class = TaskCreateSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ProjectTaskFilter
    search_fields = ('name', 'description', 'status', 'type', 'label', 'tags__name')
    ordering_fields = ('name', 'description', 'status', 'type', 'label')
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):

        return Task.objects.select_related('project', "created_by", "updated_by") \
                   .prefetch_related("activity", "tags", "members", "task_comments")\
                   .filter(project__id__in=get_my_proj(self.request.user))


    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data, context={'request': request})

        proj = get_my_proj(self.request.user)

        if serializer.is_valid():
            project = serializer.validated_data['project'].id

            if project not in proj:
                return Response(
                    {'detail':"You don't have access permissions for project with id {}".format(project)},
                    status.HTTP_403_FORBIDDEN
                )
            else:
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        # if serializer.is_valid():
        #     serializer.save()
        #
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TaskFileList(generics.ListCreateAPIView):
    serializer_class = UploadFileSerializer
    queryset = TaskPicture.objects.all()

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data, context={'request': request})
        user = request.user

        tas = [
            t.id for t in Task.objects.filter(Q(members=user) | Q(created_by=user)).all()
        ]

        if serializer.is_valid():
            task = serializer.validated_data['task'].id

            if task not in tas:
                return Response(
                    {'detail':"You don't have access permissions for task with id {}".format(task)},
                    status.HTTP_403_FORBIDDEN
                )
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TaskFileDetail(generics.GenericAPIView):
    serializer_class = UploadFileSerializer
    queryset = TaskPicture.objects.all()

    def get_object(self, pk):
        try:
            files = TaskPicture.objects.select_related("task").get(pk=pk)
        except TaskPicture.DoesNotExist:
            raise exceptions.NotFound(
                detail="File with id {} does not exist.".format(pk)
            )
        user = self.request.user
        if files.created_by != user and user not in TaskPicture.objects.all():
            raise exceptions.PermissionDenied(
                detail="You don't have access permissions for file with id {}".format(pk)
            )
        return files

    def get(self, request, pk):
        files = self.get_object(pk)
        serializer = UploadFileSerializer(files, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, pk):
        files = self.get_object(pk)
        files.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TaskDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Task instance.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_object(self, pk):
        try:
            task = Task.objects.select_related("project").get(pk=pk)
        except Task.DoesNotExist:
            raise exceptions.NotFound(
                detail="Task with id {} does not exist.".format(pk)
            )

        user = self.request.user

        if task.project.created_by != user and user not in task.project.members.all():
            raise exceptions.PermissionDenied(
                detail="You don't have access permissions for task with id {}".format(pk)
            )
        return task

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
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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

            self.queryset = activities
            response = super(ProjectActivity, self).get(request, show_type)
        except Project.DoesNotExist:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response


class ProjectDetailTag(generics.GenericAPIView):
    serializer_class = TagSerializer

    def get_project(self, pk):
        try:
            pr = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise exceptions.NotFound(
                detail="Project with id {} does not exist.".format(pk)
            )
        user = self.request.user

        if pr.created_by != user and user not in pr.members.all():
            raise exceptions.PermissionDenied(
                detail="You don't have access permissions for project with id {}".format(pk)
            )

        return pr

    def put(self, request, pk, tag_name):
        """
        Add single tag by name to the given project.
        No error will be raised in case given tag is already added.
        """
        pr = self.get_project(int(pk))

        if tag_name not in pr.tags.names():
            pr.tags.add(tag_name)

        return Response({"results": TagSerializer(pr.tags, many=True).data})

    def delete(self, request, pk, tag_name):
        """
        Remove single tag by name from the given project.
        No error will be raised in case given tag is not added to the project.
        """
        pr = self.get_project(int(pk))

        pr.tags.remove(tag_name)

        return Response({"results": TagSerializer(pr.tags, many=True).data})


class TaskDetailTag(generics.GenericAPIView):
    serializer_class = TagSerializer

    def get_project(self, pk):
        try:
            task = Task.objects.select_related("project").get(pk=pk)
        except Task.DoesNotExist:
            raise exceptions.NotFound(
                detail="Task with id {} does not exist.".format(pk)
            )
        user = self.request.user

        if task.project.created_by != user and user not in task.project.members.all():
            raise exceptions.PermissionDenied(
                detail="You don't have access permissions for task with id {}".format(pk)
            )

        return task

    def put(self, request, pk, tag_name):
        """
        Add single tag by name to the given task.
        No error will be raised in case given tag is already added to the task.
        """
        task = self.get_project(int(pk))

        if tag_name not in task.tags.names():
            task.tags.add(tag_name)

        return Response({"results": TagSerializer(task.tags, many=True).data})

    def delete(self, request, pk, tag_name):
        """
        Remove single tag by it's from the given task.
        No error will be raised in case given tag is not added to the task.
        """
        task = self.get_project(int(pk))

        task.tags.remove(tag_name)

        return Response({"results": TagSerializer(task.tags, many=True).data})


class ProjectCommentFilter(FilterSet):
     title = CharFilter(name='title', lookup_expr='exact')
     comment = CharFilter(name='comment', lookup_expr='icontains')
     project = NumberFilter(name='project__id')

     class Meta:
         model = ProjectComment
         fields = ['title', 'comment', 'project']

class ProjectCommentList(generics.ListCreateAPIView):
    serializer_class = ProjectCommentSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ProjectCommentFilter
    search_fields = ('title', 'comment')
    ordering_fields = ('title', 'id')


    def get_queryset(self):

        return ProjectComment.objects.filter(project__id__in=get_my_proj(self.request.user))

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data, context={'request': request})

        proj = get_my_proj(self.request.user)

        if serializer.is_valid():
            project = serializer.validated_data['project'].id
            if project not in proj:
                return Response(
                    {'detail':"You don't have access permissions for project with id {}".format(project)},
                    status.HTTP_403_FORBIDDEN
                )
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProjectCommentDetail(generics.GenericAPIView):
    serializer_class = ProjectCommentSerializer
    queryset = ProjectComment.objects.all()

    def get_object(self,pk):
        try:
            comment = ProjectComment.objects.select_related('project').get(pk=pk)
        except ProjectComment.DoesNotExist:
            raise exceptions.NotFound(
                detail="Comment with id {} does not exist.".format(pk)
            )

        user = self.request.user

        if comment.project.created_by != user and user not in comment.project.members.all():
            raise exceptions.PermissionDenied(
                detail="You don't have access permissions for comment with id {}".format(pk)
            )
        return comment

    def get(self, request, pk):
        comment= self.get_object(pk)
        serializer = ProjectCommentSerializer(comment, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = ProjectCommentSerializer(comment, data=request.data, context={'request': request})
        proj = get_my_proj(self.request.user)

        if serializer.is_valid():
            project = serializer.validated_data['project'].id

            if project not in proj:
                return Response(
                    {'detail':"You don't have access permissions for project with id {}".format(project)},
                    status.HTTP_403_FORBIDDEN
                )
            serializer.save()

            return Response(serializer.data)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskCommentFilter(FilterSet):
     title = CharFilter(name='title', lookup_expr='exact')
     comment = CharFilter(name='comment', lookup_expr='icontains')
     task = NumberFilter(name='task__id')

     class Meta:
         model = TaskComment
         fields = ['title', 'comment', 'task']


class TaskCommentList(generics.ListCreateAPIView):
    serializer_class = TaskCommentSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TaskCommentFilter
    search_fields = ('title', 'comment')
    ordering_fields = ('title', 'id', 'created_by__username')

    def get_queryset(self):
        current_user = self.request.user
        tas = Task.objects.select_related('project', "created_by", "updated_by") \
                  .prefetch_related("activity", "tags", "members", "task_comments")\
                  .filter(project__id__in=get_my_proj(current_user))

        return TaskComment.objects.filter(task__id__in=tas)

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data, context={'request': request})
        user = request.user

        tas = [
            t.id for t in Task.objects.select_related('project', "created_by", "updated_by") \
                              .prefetch_related("activity", "tags", "members", "task_comments")\
                              .filter(project__id__in=get_my_proj(user))
        ]

        if serializer.is_valid():
            task = serializer.validated_data['task'].id

            if task not in tas:
                return Response(
                    {'detail':"You don't have access permissions for task with id {}".format(task)},
                    status.HTTP_403_FORBIDDEN
                )
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TaskCommentDetail(generics.GenericAPIView):
    serializer_class = TaskCommentSerializer
    queryset = TaskComment.objects.all()

    def get_object(self,pk):
        try:
            comment = TaskComment.objects.select_related('task').get(pk=pk)
        except TaskComment.DoesNotExist:
            raise exceptions.NotFound(
                detail="Comment with id {} does not exist.".format(pk)
            )

        user = self.request.user

        if comment.task.created_by != user and user not in comment.task.members.all():
            raise exceptions.PermissionDenied(
                detail="You don't have access permissions for comment with id {}".format(pk)
            )
        return comment

    def get(self, request, pk):
        comment= self.get_object(pk)
        serializer = TaskCommentSerializer(comment, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = TaskCommentSerializer(comment, data=request.data, context={'request': request})
        user = self.request.user
        tas = [
            t.id for t in Task.objects.filter(Q(members=user) | Q(created_by=user)).all()
        ]
        if serializer.is_valid():
            task = serializer.validated_data['task'].id

            if task not in tas:
                return Response(
                    {'detail':"You don't have access permissions for project with id {}".format(task)},
                    status.HTTP_403_FORBIDDEN
                )
            serializer.save()

            return Response(serializer.data)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def get_projects(pr_ids, request):

    return ProjectSerializer(
        Project.objects.filter(id__in=pr_ids).all(), many=True, context={'request': request}
    ).data


def get_tasks(task_ids, request):
    tasks = Task.objects.select_related('project', "created_by", "updated_by") \
                .prefetch_related("activity", "tags", "members", "task_comments") \
                .filter(id__in=task_ids)

    return TaskSerializer(tasks, many=True, context={'request': request}).data


def get_task_comments(t_comments_ids, request):
    comments = TaskComment.objects.select_related("task")\
                          .filter(id__in=t_comments_ids)

    return TaskCommentSerializer(comments, many=True, context={'request': request}).data


class GlobalSearchView(generics.ListAPIView):
    def get(self, request, query_string):
        """
        Makes full text search by tasks, projects & task comments for given search string

        Args:
            query_string: string to search by

        Returns: object with 3 keys:

            - list of projects
            - list of tasks
            - list of task comments

        """
        func_map = {
            "project": get_projects,
            "task":get_tasks,
            "task_comment": get_task_comments
        }
        results = {k: [] for k in func_map.keys()}

        my_proj = get_my_proj(request.user)

        if not settings.USE_GLOBAL_SEARCH or not my_proj:
            return Response(results)

        try:
            for search_where in settings.SPHINX_INDEXES:
                resp = perform_search(
                    query_string,
                    index=search_where,
                    host=settings.SPHINX_SEARCH_PARAMS['host'],
                    port=settings.SPHINX_SEARCH_PARAMS['port'],
                    search_filters=[{'project_id': my_proj}],
                    mode=settings.SPHINX_SEARCH_PARAMS['mode']
                )

                if isinstance(resp, list):
                    key = search_where.replace('_rt', '')
                    results[key] = func_map[key]([int(id) for id in resp], request)
        except Exception as e:
            _logger.error(e)
            raise exceptions.APIException(detail='Some error', status=resp.status_code)

        return Response(results)