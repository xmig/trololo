from rest_framework import serializers
from django.conf import settings
from activity.models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = (
            'id', 'message', 'created_at', 'updated_at',
            'created_by', 'updated_by',
        )

        read_only_fields = (
            'id', 'message', 'created_at', 'updated_at',
            'created_by', 'updated_by',
        )

