from rest_framework import serializers
from projects.models import Project, Task, TaskComment, ProjectComment, Status
from django.contrib.auth import get_user_model
from taggit.models import Tag
from users.serializers import OnlyUserInfoSerializer


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
    # members = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name='users:single_user',
    #     queryset=get_user_model().objects.all(),
    #     required=False,
    #     lookup_field='id'
    # )
    members = OnlyUserInfoSerializer(many=True, read_only=True)

    created_by = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='users:single_user',
        required=False,
        lookup_field='id'
    )
    updated_by = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='users:single_user',
        required=False,
        lookup_field='id'
    )
    
    owner = OnlyUserInfoSerializer(source='created_by', read_only=True)

    tags = TagSerializer(many=True, read_only=False)

    class Meta:
        model = Project
        fields = (
            'name', 'id', 'description', 'status', 'members', 'comments', 'visible_by',
            'tasks', 'date_started', 'date_finished', 'created_by', 'created_at',
            'updated_by', 'updated_at', 'owner', 'tags'
        )
        read_only_fields =('created_by', 'created_at', 'updated_by', 'updated_at')

    def take_comments(self, project):
        comments_list = [x.title for x in project.projectcomment_set.all()]
        return comments_list

    def save_tags(self, instance, tags):
        if tags is not None:
            instance.tags.set(*[tag['name'] for tag in tags])
            instance.save()
            
        return instance

            
    def to_representation(self, obj):
        data = super(ProjectSerializer, self).to_representation(obj)
        data['task_count'] = Task.objects.all().filter(project=obj).count()
        data['my_task_count'] = Task.objects.all().filter(project=obj)\
            .filter(created_by=self.context['request'].user).count()

        return data

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
    activity = serializers.SerializerMethodField('take_activity')
    # comments = TaskCommentSerializer()

    project = serializers.HyperlinkedRelatedField(
        view_name='projects:projects_detail',
        queryset=Project.objects.all(),
        required=False,
        lookup_field='pk'
    )

    # project = OnlyProjectInfoSerializer(read_only=True)

    # members = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name='users:single_user',
    #     queryset=get_user_model().objects.all(),
    #     required=False,
    #     lookup_field='id'
    # )

    members = OnlyUserInfoSerializer(many=True, read_only=True) #to show names instead of urls

    created_by = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='users:single_user',
        required=False,
        lookup_field='id'
    )
    updated_by = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='users:single_user',
        required=False,
        lookup_field='id'
    )
    tags = TagSerializer(many=True, read_only=False)

    class Meta:
        model = Task
        fields = (
            'name', 'id', 'description', 'status', 'members', 'type', 'label',
            'project', 'comments', 'activity', 'deadline_date', 'estimate_minutes', 'created_by',
            'created_at', 'updated_by', 'updated_at', 'tags'
        )
        read_only_fields =('created_by', 'created_at', 'updated_by', 'updated_at')

    def take_comments(self, task):
        comments_list = [x.title for x in task.taskcomment_set.all()]
        return comments_list

    def take_activity(self, task):
        activity_list = [x.message for x in task.activity.all()]
        return activity_list
    
    def save_tags(self, instance, tags):
        if tags is not None:
            instance.tags.set(*[tag['name'] for tag in tags])
            instance.save()

        return instance

    def create(self, validated_data):
        tags = validated_data.pop('tags') if 'tags' in validated_data else None

        proj = super(TaskSerializer, self).create(validated_data)

        return self.save_tags(proj, tags)

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
        read_only_fields =('created_by', 'created_at', 'updated_by', 'updated_at')


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        read_only_fields =('created_by', 'created_at', 'updated_by', 'updated_at')


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
