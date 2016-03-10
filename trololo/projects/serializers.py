from django.contrib.auth.models import User, Group
from rest_framework import serializers


### project
from models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField('take_tasks')

    class Meta:
        model = Project
        fields = ('name', 'id', 'status', 'description', 'visible_by', 'tasks') # 'date_started', 'date_finished'

    def take_tasks(self, project):
        tasks_list = [x.task.name for x in project.task_set.all()]
        return tasks_list


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField('take_project')
    status = serializers.SerializerMethodField('take_status')
    type = serializers.SerializerMethodField('take_type')
    label = serializers.SerializerMethodField('take_label')

    class Meta:
        model = Task
        fields = ('name', 'id', 'description', 'status', 'type', 'label', 'project') # 'created_at', 'modified_at', 'deadline_date', 'estimate_minutes'

    def take_project(self, task):
        project = task.project.name
        return project

    def take_status(self, task):
        status = task.status.status
        return status

    def take_type(self, task):
        type = task.type.type
        return type

    def take_label(self, task):
        label = task.label.label
        return label