from django.db import models
from cuser.fields import CurrentUserField
import copy
from django.conf import settings

class AbstractModel(models.Model):
    class Meta:
        abstract = True


class AbstractSignable(models.Model):
    class Meta:
        abstract = True

    created_by = CurrentUserField(add_only=True, related_name="%(class)s_created_by", default='')
    updated_by = CurrentUserField(related_name="%(class)s_updated_by", default='')


class AbstractTimestampable(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AbstractAddOldObject(object):

    __original_object = None

    def __init__(self, *args, **kwargs):
        super(AbstractAddOldObject, self).__init__(*args, **kwargs)
        self.set_original_object(copy.copy(self))

    def get_original_object(self):
        return self.__original_object

    def set_original_object(self, original_object):
        self.__original_object = original_object


class HasStatus(models.Model, AbstractAddOldObject):
    class Meta:
        abstract = True

    group = models.ForeignKey(settings.STATUS_MODEL, blank=True, null=True, related_name='%(class)s_statuses')