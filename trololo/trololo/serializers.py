from django.contrib.auth.models import User, Group
from rest_framework import serializers


### project
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    # members = serializers.SerializerMethodField('take_members')

    class Meta:
        model = Project
        fields = ('name', 'id', 'description') # 'date_started', 'date_finished'

    # def take_members(self, project):
    #     members_list = [x.user.username for x in project.member_set.all()]
    #     return members_list



