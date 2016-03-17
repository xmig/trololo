from django.db import models
from django.conf import settings
from chi_django_base.models import AbstractModel, AbstractTimestampable, AbstractSignable


class HasActivity(models.Model):
    class Meta:
        abstract = True

    activity = models.ManyToManyField(settings.ACTIVITY_MODEL, null=True, blank=True, related_name='activities')

    def get_activity_message(self, **kwargs):
        return 'test message'


class Activity(AbstractModel, AbstractTimestampable, AbstractSignable):

    message = models.TextField()

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.message
