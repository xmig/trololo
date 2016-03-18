from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'specialization', 'photo', 'is_active',
            'email', 'is_superuser', 'is_staff', 'last_login',
            'department', 'detailed_info', 'date_joined'
        )

        read_only_fields = (
            'username', 'is_active', 'id',
            'is_superuser', 'is_staff',
            'last_login', 'email', 'date_joined'
        )
    # Deprecated!!!
    # def to_representation(self, obj):
    #     data = super(UserSerializer, self).to_representation(obj)
    #
    #     if data.get('photo'):
    #         print(data['photo'])
    #         data['photo'] = '/media/' + data['photo']
    #
    #     return data


class UserFilterSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    project = serializers.IntegerField(required=False)
    task = serializers.IntegerField(required=False)
