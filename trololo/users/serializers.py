from rest_framework import serializers
from django.contrib.auth import get_user_model
from trololo.gravatarintegration import get_avatavr_url
from projects.models import Project, Task
from allauth.socialaccount.models import SocialAccount


class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='projects:projects_detail',
        queryset=Project.objects.all(),
        source='projects_added',
        required=False,
        lookup_field='pk'
    )
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='tasks:tasks_detail',
        queryset=Task.objects.all(),
        source='tasks_added',
        required=False,
        lookup_field='pk'
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='users:single_user', read_only=True ,lookup_field='id'
    )

    social_accounts = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'specialization', 'photo', 'is_active',
            'email', 'is_superuser', 'is_staff', 'last_login',
            'department', 'detailed_info', 'date_joined',
            'projects', 'url', 'use_gravatar', 'tasks',
            'social_accounts'
        )

        read_only_fields = (
            'username', 'is_active', 'id',
            'is_superuser', 'is_staff',
            'last_login', 'email', 'date_joined',
            'url', 'social_accounts'
        )

    def get_social_accounts(self, user):

        return [
            acc.provider for acc in SocialAccount.objects.filter(user_id=user).all()
        ]

    def to_representation(self, obj):
        data = super(UserSerializer, self).to_representation(obj)
        if data['use_gravatar']:
            data['photo'] = get_avatavr_url(
                data['email'], default='http://www.curiousinkling.com/img/trololo/trololo-t-shirts-005DES.gif'
            )
        if not data['photo']:
            data['photo'] = 'http://www.curiousinkling.com/img/trololo/trololo-t-shirts-005DES.gif'

        return data


class OnlyUserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'specialization', 'is_active',
            'email'
        )

        read_only_fields = (
            'id', 'username', 'first_name', 'last_name',
            'specialization', 'is_active',
            'email'
        )
