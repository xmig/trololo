from django.contrib.auth.models import User, Group
from rest_framework import viewsets


# project
from models import Project
from serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all().order_by('-name')
    serializer_class = ProjectSerializer


# task
from models import Task
from serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('-name')
    serializer_class = TaskSerializer


from models import ProjectComment
from serializers import ProjectCommentSerializer

class ProjectCommentViewSet(viewsets.ModelViewSet):

    queryset = ProjectComment.objects.all().order_by('-created_at')
    serializer_class = ProjectCommentSerializer


from models import TaskComment
from serializers import TaskCommentSerializer

class TaskCommentViewSet(viewsets.ModelViewSet):

    queryset = TaskComment.objects.all().order_by('-created_at')
    serializer_class = TaskCommentSerializer