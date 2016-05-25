from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from chi_django_base.models import AbstractModel, AbstractTimestampable, AbstractSignable, AbstractAddOldObject
import logging

_logger = logging.getLogger('app')


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

        if settings.SEND_EMAIL_NOTIFICATION:
            if self.__class__.__name__ == 'Task':
                task_obj = self
            elif self.__class__.__name__ in ['TaskComment']:
                task_obj = self.task
            task_name = task_obj.name
            task_id = task_obj.id
            task_members = [t.email for t in task_obj.members.all()]

            email_body = '<b>{0}</b><br /><br />You receive this mail because of you are member of the task "{1}"'.format(
                activity_massage, task_name
            )
            for email_addr in [task_obj.created_by.email] + task_members:
                try:
                    send_mail(
                        "Changed task #{} {}".format(task_id, task_name),
                        email_body,
                        settings.EMAIL_HOST_USER,
                        [email_addr],
                        html_message=email_body
                    )
                except Exception as e:
                    _logger("Email sending error: {}".format(e))

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