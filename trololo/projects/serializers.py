from rest_framework import serializers

from projects.models import Project, Task, TaskComment, ProjectComment, Status
from django.contrib.auth import get_user_model
from taggit.models import Tag


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.SerializerMethodField('take_comments')

    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='tasks:tasks_detail',
        queryset=Task.objects.all(),
        required=False,
        lookup_field='pk'
    )
    members = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='users:single_user',
        queryset=get_user_model().objects.all(),
        required=False,
        lookup_field='id'
    )
    created_by = serializers.HyperlinkedRelatedField(
        view_name='users:single_user',
        queryset=get_user_model().objects.all(),
        required=False,
        lookup_field='id'
    )
    updated_by = serializers.HyperlinkedRelatedField(
        view_name='users:single_user',
        queryset=get_user_model().objects.all(),
        required=False,
        lookup_field='id'
    )
    new_tags = serializers.ListField(
        write_only=True,
        required=False,
        child=serializers.CharField()
    )
    tags = serializers.SerializerMethodField()

    def get_tags(self, obj):
        return obj.tags.names()

    class Meta:
        model = Project
        fields = (
            'name', 'id', 'description', 'status', 'members', 'comments', 'visible_by',
            'tasks', 'date_started', 'date_finished', 'created_by', 'created_at',
            'updated_by', 'updated_at', 'tags', 'new_tags'
        )

    def take_comments(self, project):
        comments_list = [x.comment for x in project.projectcomment_set.all()]
        return comments_list

    def save_tags(self, instance, tags):
        if tags is not None:
            instance.tags.set(*tags)
            instance.save()

        return instance

    def create(self, validated_data):
        tags = validated_data.pop('new_tags') if 'new_tags' in validated_data else None

        proj = super(ProjectSerializer, self).create(validated_data)

        return self.save_tags(self, proj, tags)

    def update(self, instance, validated_data):
        tags = validated_data.pop('new_tags') if 'new_tags' in validated_data else None

        instance = super(ProjectSerializer, self).update(instance, validated_data)

        return self.save_tags(instance, tags)


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.SerializerMethodField('take_comments')

    project = serializers.HyperlinkedRelatedField(
        view_name='projects:projects_detail',
        queryset=Project.objects.all(),
        required=False,
        lookup_field='pk'
    )
    members = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='users:single_user',
        queryset=get_user_model().objects.all(),
        required=False,
        lookup_field='id'
    )
    created_by = serializers.HyperlinkedRelatedField(
        view_name='users:single_user',
        queryset=get_user_model().objects.all(),
        required=False,
        lookup_field='id'
    )
    updated_by = serializers.HyperlinkedRelatedField(
        view_name='users:single_user',
        queryset=get_user_model().objects.all(),
        required=False,
        lookup_field='id'
    )

    class Meta:
        model = Task
        fields = ('name', 'id', 'description', 'status', 'members', 'type', 'label', 'project', 'comments', 'deadline_date', 'estimate_minutes', 'created_by', 'created_at', 'updated_by', 'updated_at')

    def take_comments(self, task):
        comments_list = [x.comment for x in task.taskcomment_set.all()]
        return comments_list


class ProjectCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectComment


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment


class StatusSerializer(serializers.ModelSerializer):

    project = serializers.HyperlinkedRelatedField(
        view_name='projects:projects_detail',
        queryset=Project.objects.all(),
        required=True,
        lookup_field='pk'
    )

    url = serializers.HyperlinkedIdentityField(
        view_name='statuses:status_detail', read_only=True ,lookup_field='pk'
    )
    class Meta:
        model = Status
        fields = ('name', 'order_number', 'url', 'project')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag