from __future__ import unicode_literals
from django.db import models


class BaseModel(models.Model):
    pass


class TaskStatus(BaseModel):
    status = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.status

    def __unicode__(self):
        return self.status


class TaskType(BaseModel):
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type

    def __unicode__(self):
        return self.type


class TaskLabel(BaseModel):
    label = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.label

    def __unicode__(self):
        return self.label


class Task(BaseModel):
    # project = relation to the project
    # members = relation for members on projects
    status = models.ForeignKey(TaskStatus)
    type = models.ForeignKey(TaskType)
    label = models.ForeignKey(TaskLabel)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deadline_date = models.DateTimeField(blank=True)
    estimate_minutes = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class TaskComment(BaseModel):
    # who = relation for project user
    task = models.ForeignKey(Task)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.comment

    def __unicode__(self):
        return self.comment


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