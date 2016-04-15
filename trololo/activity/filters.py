import django_filters
from activity.models import Activity
from rest_framework import filters


class ActivityFilter(filters.FilterSet):
    message_like = django_filters.CharFilter(name='message', lookup_expr='icontains')
    date = django_filters.DateTimeFromToRangeFilter(name='created_at')
    class Meta:
        model = Activity
        fields = ['message', 'message_like', 'date', 'created_at', 'created_by', 'project_activities']