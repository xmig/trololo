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

