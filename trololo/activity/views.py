from activity.serializers import ActivitySerializer
from activity.models import Activity
from projects.models import Project
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status

class SingleActivity(GenericAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get(self, request, id):
        """
        Get activity data by id
        """
        try:
            activity = self.get_queryset().get(pk=int(id))
            data = ActivitySerializer(activity).data
            response = Response(data)
        except Activity.DoesNotExist:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response


class ProjectActivity(GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ActivitySerializer

    def get(self, request, id):
        """
        Get project activity data by project id
        Activity ordering by created_at DESC
        """
        try:
            project = self.get_queryset().get(pk=int(id))
            activities = project.activity.all().order_by('-created_at')
            data = ActivitySerializer(activities, many=True).data
            response = Response(data)
        except Project.DoesNotExist:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
