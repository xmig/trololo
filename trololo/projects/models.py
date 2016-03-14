from __future__ import unicode_literals
from django.db import models

from users.models import TrololoUser


class Project(models.Model):

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
    owner = models.ForeignKey(TrololoUser, blank=True, default='')
    member = models.ManyToManyField(TrololoUser, blank=True, default='')
    status = models.CharField(max_length=30, choices=STATUSES, default=UNDEFINED)
    description = models.TextField(max_length=1000, null=True, blank=True, default='')
    visible_by = models.CharField(max_length=30, choices=VISIBILITY, default=UNDEFINED)
    date_started = models.DateTimeField(blank=True, null=True, default='')
    date_finished = models.DateTimeField(blank=True, null=True, default='')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ProjectComment(models.Model):
    # who = relation for project user
    project = models.ForeignKey(Project, blank=True, null=True, default='')
    comment = models.TextField(blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def __unicode__(self):
        return self.comment



class Task(models.Model):

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
        (RED, "Breakthrough"),
        (ORANGE, "In_progress"),
        (GREEN, "Finished"),
        (UNDEFINED, "Undefined"),

    )

    project = models.ForeignKey(Project, default='', blank=True)
    # members
    status = models.CharField(max_length=30, choices=STATUSES, default=UNDEFINED, help_text='choose status')
    type = models.CharField(max_length=30, choices=TYPES, default=UNDEFINED, help_text='choose type')
    label = models.CharField(max_length=50, choices=LABELS, default=UNDEFINED, help_text='choose label')

    name = models.CharField(max_length=150, null=True, default='', blank=True)
    description = models.TextField(blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deadline_date = models.DateTimeField(null=True, blank=True, default='')
    estimate_minutes = models.IntegerField(null=True, blank=True, default='')


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class TaskComment(models.Model):
    # who = relation for project user
    task = models.ForeignKey(Task)
    comment = models.TextField(blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def __unicode__(self):
        return self.comment