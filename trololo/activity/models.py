from django.db import models
from django.conf import settings
from chi_django_base.models import AbstractModel, AbstractTimestampable, AbstractSignable, AbstractAddOldObject


class HasActivity(models.Model, AbstractAddOldObject):
    class Meta:
        abstract = True

    activity = models.ManyToManyField(settings.ACTIVITY_MODEL, blank=True, related_name='%(class)s_activities')

    def get_activity_message_on_create(self, **kwargs):
        return 'create activity default message'

    def get_activity_message_on_update(self, **kwargs):
        return 'update activity default message'

    def __get_activity_message(self, **kwargs):
        if self.pk is None:
            return self.get_activity_message_on_create()
        else:
            return self.get_activity_message_on_update()

    def __get_activity_model_name(self, **kwargs):
        return self.__class__.__name__.lower()

    def save(self, *args, **kwargs):
        activity_massage = self.__get_activity_message(**kwargs)
        activity_model_name = self.__get_activity_model_name(**kwargs)
        super(HasActivity, self).save(*args, **kwargs)
        self.activity.create(message=activity_massage, activity_model=activity_model_name)


class Activity(AbstractModel, AbstractTimestampable, AbstractSignable):

    message = models.TextField()
    activity_model = models.CharField(max_length=30)

    ordering = ['-created_at']

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.message