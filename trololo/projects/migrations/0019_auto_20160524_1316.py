# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
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
            model_name='status',
            name='activity',
            field=models.ManyToManyField(related_name='status_activities', to='activity.Activity', blank=True),
        ),
        migrations.AddField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 13, 15, 54, 363471, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='created_by',
            field=cuser.fields.CurrentUserField(related_name='status_created_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 13, 16, 1, 165970, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='status_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
