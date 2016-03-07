from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # username = serializers.CharField(max_length=100)
    class Meta:
        model = User
        # fields = (
        #     'id', 'username', 'is_superuser', 'last_login',
        #     'email', 'is_active', 'is_staff'
        # )
        fields = '__all__'