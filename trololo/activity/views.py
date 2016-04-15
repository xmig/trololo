from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import status
from django.db.models import Q
from rest_framework import filters
from activity.serializers import ActivitySerializer
from activity.models import Activity
from activity.filters import ActivityFilter
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


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


class Activities(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_class = ActivityFilter
    ordering_fields = ('message', 'created_at',)
    ordering = ('-created_at',)

    def get(self, request, show_type):
        """
        Get activities data by show_type \n
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

            if show_type == 'a':
                # all activity
                activity_type_query = Q(project_activities__gt=0) | Q(task_activities__gt=0)
            elif show_type == 'p':
                # project only activity
                activity_type_query = Q(project_activities__gt=0)
            elif show_type == 't':
                # task only activity
                activity_type_query = Q(task_activities__gt=0)
            else:
                activity_type_query = Q(project_activities__gt=0) | Q(task_activities__gt=0)

            activities = self.get_queryset().filter(activity_type_query)

            if for_current_user:
                activities = activities.filter(created_by=int(request.user.id))

            self.queryset = activities
            response = super(Activities, self).get(request, show_type)
        except Activity.DoesNotExist:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
