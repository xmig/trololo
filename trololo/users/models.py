from django.db import models
from django.contrib.auth.models import AbstractUser


class TrololoUser(AbstractUser):
    photo = models.ImageField()
    department = models.CharField(max_length=40)
    specialization = models.CharField(max_length=200)
    detailed_info = models.TextField()
