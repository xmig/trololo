from rest_framework import serializers

from projects.models import Project, Task, TaskComment, ProjectComment
from django.contrib.auth import get_user_model


class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField('take_tasks')
    members = serializers.SerializerMethodField('take_members')
    comments = serializers.SerializerMethodField('take_comments')

    class Meta:
        model = Project
        fields = ('name', 'id', 'status', 'description', 'owner', 'members', 'visible_by', 'tasks', 'comments', 'date_started', 'date_finished')

    def take_tasks(self, project):
        tasks_list = [x.name for x in project.task_set.all()]
        return tasks_list

    def take_comments(self, project):
        comments_list = [x.comment for x in project.projectcomment_set.all()]
        return comments_list

    def take_members(self, project):
        members_list = [x.username for x in project.members.all()]
        return members_list


class TaskSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField('take_comments')

    class Meta:
        model = Task
        fields = ('name', 'id', 'description', 'status', 'type', 'label', 'project', 'comments', 'created_at', 'modified_at', 'deadline_date', 'estimate_minutes')

    def take_comments(self, task):
        comments_list = [x.comment for x in task.taskcomment_set.all()]
        return comments_list



class ProjectCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectComment


class TaskCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskComment

