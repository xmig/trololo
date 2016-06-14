from django.db import models
from django.utils import timezone


class ClusterBaseModel(models.Model):
    """
    Base Model for all models
    """
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ClusterInfo(ClusterBaseModel):
    host_ip = models.CharField(max_length=100, null=True, blank=True)
    internal_ip = models.CharField(max_length=100, null=True, blank=True)
    hostname = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True, default="")
    in_cluster = models.BooleanField(default=False)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.host_ip

    def __unicode__(self):
        return self.host_ip