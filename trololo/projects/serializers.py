from django.contrib.auth.models import User, Group
from rest_framework import serializers

from models import Project, Task, TaskComment, ProjectComment


class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField('take_tasks')
    comments = serializers.SerializerMethodField('take_comments')

    class Meta:
        model = Project
        fields = ('name', 'id', 'status', 'description', 'visible_by', 'tasks', 'comments', 'date_started', 'date_finished')

    def take_tasks(self, project):
        tasks_list = [x.name for x in project.task_set.all()]
        return tasks_list

    def take_comments(self, project):
        comments_list = [x.comment for x in project.projectcomment_set.all()]
        return comments_list


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField('take_project')
    comments = serializers.SerializerMethodField('take_comments')

    class Meta:
        model = Task
        fields = ('name', 'id', 'description', 'status', 'type', 'label', 'project', 'comments', 'created_at', 'modified_at', 'deadline_date', 'estimate_minutes')

    def take_project(self, task):
        project = task.project.name
        return project

    def take_comments(self, task):
        comments_list = [x.comment for x in task.taskcomment_set.all()]
        return comments_list



class ProjectCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectComment


class TaskCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskComment




    # def take_status(self, task):
    #     status = task.status.status
    #     return status
    #
    # def take_type(self, task):
    #     type = task.type.type
    #     return type
    #
    # def take_label(self, task):
    #     label = task.label.label
    #     return label




        TrololoUser