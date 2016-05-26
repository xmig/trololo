# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import projects.models
from django.utils.timezone import utc
from django.conf import settings
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_activity_activity_model'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0018_auto_20160520_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskpicture',
            name='activity',
            field=models.ManyToManyField(related_name='taskpicture_activities', to='activity.Activity', blank=True),
        ),
        migrations.AddField(
            model_name='taskpicture',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 26, 15, 6, 40, 903335, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskpicture',
            name='created_by',
            field=cuser.fields.CurrentUserField(related_name='taskpicture_created_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='taskpicture',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 26, 15, 6, 44, 598957, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskpicture',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='taskpicture_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='taskpicture',
            name='file_upload',
            field=models.FileField(upload_to=projects.models.task_directory_path),
        ),
        migrations.AlterField(
            model_name='taskpicture',
            name='task',
            field=models.ForeignKey(related_name='files', blank=True, to='projects.Task', null=True),
        ),
    ]
