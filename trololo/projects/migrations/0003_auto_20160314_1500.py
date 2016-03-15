# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_task_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='member',
            field=models.ManyToManyField(related_name='projects_added', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(related_name='projects_owned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='member',
            field=models.ManyToManyField(related_name='tasks_added', to=settings.AUTH_USER_MODEL),
        ),
    ]
