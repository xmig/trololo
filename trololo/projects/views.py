from serializers import ProjectSerializer, TaskSerializer # ProjectCommentSerializer, TaskCommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from projects.models import Project, Task

from rest_framework import permissions
from projects.permissions import IsOwnerOrReadOnly



class ProjectsData(GenericAPIView):
    """
    Get/Update data.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def get(self, request):

        # return Response(
        #     ProjectSerializer(self.get_queryset(), many=True).data
        # )

        if request.method == 'GET':
            queryset = Project.objects.all()
            serializer = ProjectSerializer(queryset, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    # def put(self,request):
    #     s = self.get_serializer_class()(request.project, data=request.data)
    #
    #     if s.is_valid():
    #         s.save()
    #
    #         return Response(s.data, status=status.HTTP_201_CREATED)
    #     return Response({"errors": s.errors}, status=status.HTTP_400_BAD_REQUEST)


class TasksData(GenericAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request):

        return Response(
            TaskSerializer(self.get_queryset(), many=True).data
        )



    #
    #
    #
    # def get(self, request, format=None):
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


