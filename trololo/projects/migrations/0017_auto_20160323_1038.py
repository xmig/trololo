# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0016_auto_20160323_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 23, 10, 38, 15, 350300, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='created_by',
            field=cuser.fields.CurrentUserField(related_name='task_created_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 23, 10, 38, 19, 62620, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='task_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='activity',
            field=models.ManyToManyField(related_name='project_activities', to='activity.Activity', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projects_added', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='activity',
            field=models.ManyToManyField(related_name='task_activities', to='activity.Activity', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='members',
            field=models.ManyToManyField(related_name='tasks_added', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
