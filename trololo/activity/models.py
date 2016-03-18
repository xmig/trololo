from django.db import models
from django.conf import settings
from chi_django_base.models import AbstractModel, AbstractTimestampable, AbstractSignable


class HasActivity(models.Model):
    class Meta:
        abstract = True

    activity = models.ManyToManyField(settings.ACTIVITY_MODEL, null=True, blank=True, related_name='activities')

    def get_activity_message_on_create(self, **kwargs):
        return 'create activity default message'

    def get_activity_message_on_update(self, **kwargs):
        return 'update activity default message'

    def __get_activity_message(self, **kwargs):
        if self.pk is None:
            return self.get_activity_message_on_create()
        else:
            return self.get_activity_message_on_update()

    def save(self, *args, **kwargs):
        activity_massage = self.__get_activity_message(**kwargs)
        super(HasActivity, self).save(*args, **kwargs)
        self.activity.create(message=activity_massage)


class Activity(AbstractModel, AbstractTimestampable, AbstractSignable):

    message = models.TextField()

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.message
