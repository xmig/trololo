from rest_framework import serializers
from models import ClusterInfo



class ClusterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterInfo
        fields = ('id',
                  'host_ip',
                  'internal_ip',
                  'hostname',
                  'description',
                  'in_cluster',
                  'enabled',)
