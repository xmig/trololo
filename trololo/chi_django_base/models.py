from django.db import models
from cuser.fields import CurrentUserField


class AbstractModel(models.Model):
    class Meta:
        abstract = True


class AbstractSignable(models.Model):
    class Meta:
        abstract = True

    created_by = CurrentUserField(add_only=True, related_name="created_by")
    updated_by = CurrentUserField(related_name="updated_by")


class AbstractTimestampable(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)