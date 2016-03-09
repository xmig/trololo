from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # username = serializers.CharField(max_length=100)
    class Meta:
        model = get_user_model()
        # fields = (
        #     'id', 'username', 'is_superuser', 'last_login',
        #     'email', 'is_active', 'is_staff'
        # )
        fields = '__all__'