from serializers import ProjectSerializer, TaskSerializer # ProjectCommentSerializer, TaskCommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from projects.models import Project, Task



class ProjectData(GenericAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request):

        return Response(
            ProjectSerializer(self.get_queryset(), many=True).data
        )

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