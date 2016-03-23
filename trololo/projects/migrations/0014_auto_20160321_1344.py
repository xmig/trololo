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
        ('projects', '0013_auto_20160318_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 21, 13, 44, 35, 223149, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=cuser.fields.CurrentUserField(related_name='project_created_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 21, 13, 44, 53, 596849, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='project_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
