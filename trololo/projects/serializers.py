from rest_framework import serializers
from projects.models import Project, Task, TaskComment, ProjectComment, Status
from django.contrib.auth import get_user_model
from taggit.models import Tag


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Tag
        fields = ['name']


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

    tags = TagSerializer(many=True, read_only=False)

    class Meta:
        model = Project
        fields = (
            'name', 'id', 'description', 'status', 'members', 'comments', 'visible_by',
            'tasks', 'date_started', 'date_finished', 'created_by', 'created_at',
            'updated_by', 'updated_at', 'tags'
        )

    def take_comments(self, project):
        comments_list = [x.title for x in project.projectcomment_set.all()]
        return comments_list

    def save_tags(self, instance, tags):
        if tags is not None:
            instance.tags.set(*[tag['name'] for tag in tags])
            instance.save()

        return instance

    def create(self, validated_data):
        tags = validated_data.pop('tags') if 'tags' in validated_data else None
        proj = super(ProjectSerializer, self).create(validated_data)

        return self.save_tags(self, proj, tags)

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags') if 'tags' in validated_data else None

        instance = super(ProjectSerializer, self).update(instance, validated_data)

        return self.save_tags(instance, tags)

    def to_representation(self, instance):
        data = super(ProjectSerializer, self).to_representation(instance)

        data['tags'] = sorted(data['tags'])
        return data


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
    tags = TagSerializer(many=True, read_only=False)

    class Meta:
        model = Task
        fields = (
            'name', 'id', 'description', 'status', 'members', 'type', 'label',
            'project', 'comments', 'deadline_date', 'estimate_minutes', 'created_by',
            'created_at', 'updated_by', 'updated_at', 'tags'
        )

    def take_comments(self, task):
        comments_list = [x.title for x in task.taskcomment_set.all()]
        return comments_list

    def save_tags(self, instance, tags):
        if tags is not None:
            instance.tags.set(*[tag['name'] for tag in tags])
            instance.save()

        return instance

    def create(self, validated_data):
        tags = validated_data.pop('tags') if 'tags' in validated_data else None

        proj = super(TaskSerializer, self).create(validated_data)

        return self.save_tags(self, proj, tags)

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags') if 'tags' in validated_data else None

        instance = super(TaskSerializer, self).update(instance, validated_data)

        return self.save_tags(instance, tags)

    def to_representation(self, instance):
        data = super(TaskSerializer, self).to_representation(instance)

        data['tags'] = sorted(data['tags'])
        return data


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