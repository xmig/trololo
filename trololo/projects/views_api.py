from django.contrib.auth.models import User, Group
from rest_framework import viewsets


# project
from models import Project
from serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('-name')
    serializer_class = ProjectSerializer


# task
from models import Task
from serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-name')
    serializer_class = TaskSerializer