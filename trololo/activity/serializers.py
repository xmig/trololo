from rest_framework import serializers
from activity.models import Activity
from users.serializers import OnlyUserInfoSerializer


class ActivitySerializer(serializers.ModelSerializer):
    owner = OnlyUserInfoSerializer(source='created_by', read_only=True)
    class Meta:
        model = Activity
        fields = (
            'id', 'message', 'created_at', 'updated_at',
            'created_by', 'updated_by', 'owner', 'activity_model'
        )

        read_only_fields = (
            'id', 'message', 'created_at', 'updated_at',
            'created_by', 'updated_by', 'owner', 'activity_model'
        )

