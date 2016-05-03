from rest_framework import serializers
from projects.models import Project, Task, TaskComment, ProjectComment, Status
from taggit.models import Tag
from users.serializers import OnlyUserInfoSerializer
from activity.serializers import ActivitySerializer
from django.db.models import Q
from django.contrib.auth import get_user_model


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Tag
        fields = ['name']


class ShortProjectInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'name', 'status',
            'date_started', 'date_finished',
            'visible_by'
        )

        read_only_fields = (
            'id', 'name', 'status',
            'date_started', 'date_finished',
            'visible_by'
        )


class ProjectCommentSerializer(serializers.ModelSerializer):
    project = serializers.HyperlinkedRelatedField(
        view_name='projects:projects_detail',
        queryset=Project.objects.all(),
        lookup_field='pk'
    )

    created_by = OnlyUserInfoSerializer(read_only=True)
    # created_by = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='users:single_user',
    #     required=False,
    #     lookup_field='id'
    # )
    updated_by = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='users:single_user',
        required=False,
        lookup_field='id'
    )

    class Meta:
        model = ProjectComment
        fields = (
            'title', 'comment', 'id', 'project', 'created_by',
            'created_at', 'updated_by', 'updated_at', 'activity'
        )
        read_only_fields =('created_by', 'created_at', 'updated_by', 'updated_at', 'activity')


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

    order_number = serializers.IntegerField(required=False)

    class Meta:
        model = Status
        fields = ('name', 'order_number', 'url', 'project', 'id')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.SerializerMethodField('take_activity')
    # activity = ActivitySerializer(source='task_comments', many=True)
    comments = ProjectCommentSerializer(source='project_comments', many=True, required=False) # display dicts of comments
    project_obj = ShortProjectInfoSerializer(source='project', read_only=True)

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
    members_data = OnlyUserInfoSerializer(source='members', many=True, read_only=True)

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

    tags = TagSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Project
        fields = (
            'name', 'id', 'description', 'status', 'members', 'comments', 'visible_by',
            'tasks', 'date_started', 'date_finished', 'created_by', 'created_at',
            'updated_by', 'updated_at', 'owner', 'tags', 'project_obj', 'activity', 'members_data'
        )
        read_only_fields =('created_by', 'created_at', 'updated_by', 'updated_at')

    def take_activity(self, project):
        activity_list = [x.message for x in project.activity.all()]
        return activity_list

    def take_comments(self, project):
        comments_list = [x.title for x in project.projectcomment_set.all()]
        return comments_list

    def save_tags(self, instance, tags):
        if tags is not None:
            instance.tags.set(*[tag['name'] for tag in tags])

        return instance

    def create(self, validated_data):
        tags = validated_data.pop('tags') if 'tags' in validated_data else None
        proj = super(ProjectSerializer, self).create(validated_data)

        stat = Status(
            project=proj,
            order_number=1,
            name='Default status'
        )

        stat.save()

        return self.save_tags(proj, tags)

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags') if 'tags' in validated_data else None

        instance = super(ProjectSerializer, self).update(instance, validated_data)

        return self.save_tags(instance, tags)

    def to_representation(self, instance):
        data = super(ProjectSerializer, self).to_representation(instance)

        data['task_count'] = Task.objects.all().filter(project=instance).count()
        data['my_task_count'] = Task.objects.all().filter(project=instance)\
            .filter(created_by=self.context['request'].user).count()

        data['tags'] = sorted(data['tags'])
        return data


# class ShortProjectInfoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Project
#         fields = (
#             'id', 'name', 'status',
#             'date_started', 'date_finished',
#             'visible_by'
#         )
#
#         read_only_fields = (
#             'id', 'name', 'status',
#             'date_started', 'date_finished',
#             'visible_by'
#         )


class TaskCommentSerializer(serializers.ModelSerializer):

    task = serializers.HyperlinkedRelatedField(
        view_name='tasks:tasks_detail',
        queryset=Task.objects.all(),
        required=False,
        lookup_field='pk'
    )

    created_by = OnlyUserInfoSerializer(read_only=True)
    # created_by = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='users:single_user',
    #     required=False,
    #     lookup_field='id'
    # )

    updated_by = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='users:single_user',
        required=False,
        lookup_field='id'
    )

    class Meta:
        model = TaskComment
        unique_together = ('task')
        fields = (
            'title', 'comment', 'id', 'task', 'created_by',
            'created_at', 'updated_by', 'updated_at', 'activity'
        )
        read_only_fields =('created_by', 'created_at', 'updated_by', 'updated_at', 'activity', 'id')


class GroupRelatedField(serializers.RelatedField):
    def get_queryset(self):
        """
        Used to get filtered by user list of statuses in browsable API
        """
        user = self.context['request'].user
        proj = [
            pr.id for pr in Project.objects.filter(Q(members=user) | Q(created_by=user)).all()
        ]
        return Status.objects.filter(project__id__in=proj)

    def to_internal_value(self, data):
        try:
            status = self.get_queryset().get(id=data)
        except Status.DoesNotExist:
            raise serializers.ValidationError(detail="Incorrect tasks group id.")
        return status

    def to_representation(self, value):
        return value.id


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.SerializerMethodField('take_activity')
    # activity = ActivitySerializer(source='task_comments', many=True)
    comments = TaskCommentSerializer(source='task_comments', many=True, read_only=True) # display dicts of comments
    project_obj = ShortProjectInfoSerializer(source='project', read_only=True)
    project = serializers.HyperlinkedRelatedField(
        view_name='projects:projects_detail',
        queryset=Project.objects.all(),
        required=False,
        lookup_field='pk'
    )

    members_info = OnlyUserInfoSerializer(source='members', many=True, read_only=True) # to display names instead of urls
    members = serializers.PrimaryKeyRelatedField(
        many=True,
        # view_name='users:single_user',
        queryset=get_user_model().objects.all(),
        required=False,
        # lookup_field='id'
    )

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

    group = GroupRelatedField(required=False, write_only=True, queryset=Status.objects.all())
    # group = serializers.PrimaryKeyRelatedField(
    #     read_only=False,
    #     required=False,
    #     queryset=Status.objects.all()
    # )
    group_data = StatusSerializer(source='group', read_only=True)

    tags = TagSerializer(many=True, read_only=False, required=False)

    owner = OnlyUserInfoSerializer(source='created_by', read_only=True)

    class Meta:
        model = Task
        fields = (
            'name', 'id', 'description', 'status', 'members_info', 'type', 'label',
            'project', 'comments', 'activity', 'deadline_date', 'estimate_minutes', 'created_by',
            'created_at', 'updated_by', 'updated_at', 'tags', 'owner', 'project_obj', 'group', 'group_data', 'members'
        )
        read_only_fields =('created_by', 'created_at', 'updated_by', 'updated_at', 'group_data')

    # def take_comments(self, task):
    #     comments_list = [x.title for x in task.taskcomment_set.all()]
    #     return comments_list

    # def take_activity(self, task):
    #     activity_list = [x.message for x in task.activity.all()]
    #     return activity_list

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

