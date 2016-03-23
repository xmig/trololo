from django.db import models
from django.contrib.auth.models import AbstractUser


def user_photo_directory_path(object, filename):
    return 'user_{0}/{1}'.format(object.id,filename)


class TrololoUser(AbstractUser):
    photo = models.ImageField(upload_to=user_photo_directory_path, blank=True)
    department = models.CharField(max_length=40, blank=True)
    specialization = models.CharField(max_length=200, blank=True)
    detailed_info = models.TextField(blank=True)
    use_gravatar = models.BooleanField(default=False)


