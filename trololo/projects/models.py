from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from activity.models import HasActivity
from chi_django_base.models import AbstractModel, AbstractTimestampable, AbstractSignable, HasStatus


class Project(AbstractModel, HasActivity, AbstractTimestampable, AbstractSignable):

    BREAKTHROUGH = "breakthrough"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    UNDEFINED = "undefined"

    STATUSES = (
        (BREAKTHROUGH, "Breakthrough"),
        (IN_PROGRESS, "In_progress"),
        (FINISHED, "Finished"),
        (UNDEFINED, "Undefined"),
    )

    MEMBERS = "members"
    PARTICULAR_USER = "particular_user"
    ALL_USERS = "all_users"
    UNDEFINED = "undefined"

    VISIBILITY = (
        (MEMBERS, "Members"),
        (PARTICULAR_USER, "Particular_user"),
        (ALL_USERS, "All_users"),
        (UNDEFINED, "Undefined"),
    )

    name = models.CharField(max_length=100, null=True, blank=True, default='')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='projects_added')
    status = models.CharField(max_length=30, choices=STATUSES, default=UNDEFINED)
    description = models.TextField(max_length=1000, null=True, blank=True, default='')
    visible_by = models.CharField(max_length=30, choices=VISIBILITY, default=UNDEFINED)
    date_started = models.DateTimeField(blank=True, null=True, default='')
    date_finished = models.DateTimeField(blank=True, null=True, default='')

    def get_activity_message_on_create(self, **kwargs):
        return 'create new project "' + self.name + '"'

    def get_activity_message_on_update(self, **kwargs):
        message = 'edit project'
        old_data = self.get_original_object()
        if old_data.name != self.name:
            message = message + ' Name: "' + old_data.name + '" ==> "' + self.name + '"'
        return message

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name



class ProjectComment(AbstractModel, HasActivity, AbstractTimestampable, AbstractSignable):
    title = models.CharField(max_length=200, blank=True, null=True, default='')
    project = models.ForeignKey(Project, blank=True, null=True, default='')
    comment = models.TextField(blank=True, null=True, default='')

    def get_activity_message_on_create(self, **kwargs):
        return 'create new comment' + self.title + 'for project' + self.project

    def get_activity_message_on_update(self, **kwargs):
        message = 'edit comment'
        old_data = self.get_original_object()
        if old_data.comment != self.comment:
            message = message + 'Comment:' + old_data.comment + ' ==> ' + self.comment
        return message

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



class Task(AbstractModel, HasActivity, AbstractTimestampable, AbstractSignable, HasStatus):

    BREAKTHROUGH = "breakthrough"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    UNDEFINED = "undefined"

    STATUSES = (
        (BREAKTHROUGH, "Breakthrough"),
        (IN_PROGRESS, "In_progress"),
        (FINISHED, "Finished"),
        (UNDEFINED, "Undefined"),
    )

    BUG = "bug"
    FEATURE = "feature"
    UNDEFINED = "undefined"

    TYPES = (
        (BUG, "Bug"),
        (FEATURE, "Feature"),
        (UNDEFINED, "Undefined"),
    )

    RED = "red"
    ORANGE = "orange"
    GREEN = "green"
    UNDEFINED = "undefined"

    LABELS = (
        (RED, "Red"),
        (ORANGE, "Orange"),
        (GREEN, "Green"),
        (UNDEFINED, "Undefined"),
    )

    name = models.CharField(max_length=150, null=True, default='', blank=True)
    description = models.TextField(blank=True, null=True, default='')
    project = models.ForeignKey(Project, default='', null=True, blank=True, related_name='tasks')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='tasks_added')
    status = models.CharField(max_length=30, choices=STATUSES, default=UNDEFINED, help_text='choose status')
    type = models.CharField(max_length=30, choices=TYPES, default=UNDEFINED, help_text='choose type')
    label = models.CharField(max_length=50, choices=LABELS, default=UNDEFINED, help_text='choose label')
    deadline_date = models.DateTimeField(null=True, blank=True, default='')
    estimate_minutes = models.IntegerField(null=True, blank=True, default='')

    def get_activity_message_on_create(self, **kwargs):
        return 'create new task "' + self.name + '"'

    def get_activity_message_on_update(self, **kwargs):
        message = 'edit task'
        old_data = self.get_original_object()
        if old_data.name != self.name:
            message = message + ' Name: "' + old_data.name + '" ==> "' + self.name + '"'
        return message

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name



class TaskComment(AbstractModel, HasActivity, AbstractTimestampable, AbstractSignable):
    title = models.CharField(max_length=200, blank=True, null=True, default='')
    task = models.ForeignKey(Task, default='', null=True, blank=True)
    comment = models.TextField(blank=True, null=True, default='')

    def get_activity_message_on_create(self, **kwargs):
        return 'create new comment' + self.title + 'for task' + self.task

    def get_activity_message_on_update(self, **kwargs):
        message = 'edit comment'
        old_data = self.get_original_object()
        if old_data.comment != self.comment:
            message = message + 'Comment:' + old_data.comment + ' ==> ' + self.comment
        return message

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Status(AbstractModel):

    project = models.ForeignKey(Project, default=True, null=True, blank=True, related_name='project_statuses')
    name = models.CharField(max_length=30)
    order_number = models.IntegerField()
    ordering = ['-order_number']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
