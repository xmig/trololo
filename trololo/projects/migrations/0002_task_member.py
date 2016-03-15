# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='member',
            field=models.ManyToManyField(default='', related_name='tasks_added', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
