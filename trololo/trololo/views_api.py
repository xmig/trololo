from django.contrib.auth.models import User, Group
from rest_framework import viewsets


# project
from projects.models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('-name')
    serializer_class = ProjectSerializer