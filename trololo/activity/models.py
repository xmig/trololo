from django.db import models
from django.conf import settings
from chi_django_base.models import AbstractModel, AbstractTimestampable, AbstractSignable, AbstractAddOldObject
import logging
from activity import tasks
from django.contrib.sites.models import Site

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

        super(HasActivity, self).save(*args, **kwargs)

        if settings.SEND_EMAIL_NOTIFICATION:
            task_obj = None
            if self.__class__.__name__ == 'Task':
                task_obj = self
            elif self.__class__.__name__ in ['TaskComment', 'TaskPicture']:
                task_obj = self.task

            if task_obj:
                task_name = task_obj.name
                task_id = task_obj.id
                task_members = [t.email for t in task_obj.members.all()]

                email_body = '<b>{0}</b><br /><br />You receive this mail because of you are member of the task "{1}"'.format(
                    activity_massage, task_name
                )

                site = Site.objects.filter(id=settings.SITE_ID).first()

                email_subject = "[{}] Changed task #{} {}".format(
                    site.name if site else '', task_id, task_name
                )
                recipients = task_members
                created_by_email = task_obj.created_by.email

                if created_by_email not in recipients:
                    recipients.append(created_by_email)
                sender = settings.EMAIL_HOST_USER
                tasks.send_emails.delay(recipients, email_subject, email_body, sender)

        self.activity.create(message=activity_massage, activity_model=activity_model_name)


class Activity(AbstractModel, AbstractTimestampable, AbstractSignable):

    message = models.TextField()
    activity_model = models.CharField(max_length=30)

    ordering = ['-created_at']

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.message