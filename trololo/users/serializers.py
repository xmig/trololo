from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='projects:projects',
        read_only=True,
        source='projects_added'
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='users:single_user', read_only=True ,lookup_field='id'
    )

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'specialization', 'photo', 'is_active',
            'email', 'is_superuser', 'is_staff', 'last_login',
            'department', 'detailed_info', 'date_joined'
            'projects', 'url'
        )

        read_only_fields = (
            'username', 'is_active', 'id',
            'is_superuser', 'is_staff',
            'last_login', 'email', 'date_joined',
            'projects', 'url'
        )
    # TODO: update this for gravatar integration
    # def to_representation(self, obj):
    #     data = super(UserSerializer, self).to_representation(obj)
    #
    #     if data.get('photo'):
    #         print(data['photo'])
    #         data['photo'] = '/media/' + data['photo']
    #
    #     return data