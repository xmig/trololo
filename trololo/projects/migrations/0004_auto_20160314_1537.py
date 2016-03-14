# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20160314_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='member',
            field=models.ManyToManyField(related_name='projects_added', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(related_name='projects_owned', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='member',
            field=models.ManyToManyField(related_name='tasks_added', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
