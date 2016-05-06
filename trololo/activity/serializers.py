from rest_framework import serializers
from activity.models import Activity
from users.serializers import OnlyUserInfoSerializer


class ActivitySerializer(serializers.ModelSerializer):
    owner = OnlyUserInfoSerializer(source='created_by', read_only=True)

    project = serializers.SerializerMethodField()
    task = serializers.SerializerMethodField()

    def get_project(self, inst):
        proj = inst.project_activities.all()
        return {'id': proj[0].id, 'name': proj[0].name} if proj else None

    def get_task(self, inst):
        tasks = inst.task_activities.all()
        return {'id': tasks[0].id, 'name': tasks[0].name} if tasks else None

    class Meta:
        model = Activity
        fields = (
            'id', 'message', 'created_at', 'updated_at',
            'created_by', 'updated_by', 'owner', 'activity_model',
            'project', 'task'
        )

        read_only_fields = (
            'id', 'message', 'created_at', 'updated_at',
            'created_by', 'updated_by', 'owner', 'activity_model',
            'project', 'task'
        )

