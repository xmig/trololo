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
        editable_fields = (
            'first_name', 'last_name',
            'specialization', 'photo',
            'department', 'detailed_info',
        )

        read_only_fields = tuple(set(fields) - set(editable_fields))
