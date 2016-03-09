from __future__ import unicode_literals
from django.db import models


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

    # owner = models.ForeignKey(User, blank=True, default='')
    # member = models.ManyToManyField(User, blank=True, default='')
    # status = models.CharField(max_length=30, choices=STATUSES, default=UNDEFINED)

    description = models.TextField(max_length=1000, null=True, blank=True, default='')

    # visible_by = models.CharField(max_length=30, choices=VISIBILITY, default=UNDEFINED) #widget=forms.CheckboxSelectMultiple

    # date_started = models.DateField(null=True, blank=True, default='')
    # date_finished = models.DateField(null=True, blank=True, default='')



    # comments? activity?


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name