from chi_django_base.storage import OverwriteStorage
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files import File
from chi_django_base.helpers import generate_image, resize_logo
import os
from uuid import uuid4


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
        if self.photo:
            resize_logo(self)
        else:
            file_ext = '.jpeg'
            file_name = str(self.id) + str(uuid4()) + file_ext
            file_path = os.path.join('/tmp', file_name)
            if self.first_name or self.last_name:
                text = ''.join(
                    [getattr(self, attr)[0].upper() for attr in ("first_name", "last_name") if getattr(self, attr)]
                )
            else:
                text = self.username[0].upper()
            generate_image(text, file_path)

            with open(file_path, 'rb') as f:
                file_to_save = File(f)
                self.photo.save('logo' + file_ext, file_to_save, save=False)

        super(TrololoUser, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']




