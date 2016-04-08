from chi_django_base.storage import OverwriteStorage
from django.contrib.auth.models import AbstractUser
from django.db import models
from trololo.helpers import resize_logo


def user_photo_directory_path(object, filename):
    filename = 'logo.{0}'.format(filename.split('.')[-1]) if '.' in filename else 'logo'

    return 'user_{0}/{1}'.format(object.id, filename)


class TrololoUser(AbstractUser):
    photo = models.ImageField(upload_to=user_photo_directory_path, blank=True, storage=OverwriteStorage())
    department = models.CharField(max_length=40, blank=True)
    specialization = models.CharField(max_length=200, blank=True)
    detailed_info = models.TextField(blank=True)
    use_gravatar = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(TrololoUser, self).save(*args, **kwargs)

        if self.photo:
            resize_logo(self)

    class Meta:
        ordering = ['id']




