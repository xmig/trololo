# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20160324_0852'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_auto_20160331_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcomment',
            name='activity',
            field=models.ManyToManyField(related_name='projectcomment_activities', to='activity.Activity', blank=True),
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 12, 16, 3, 991175, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='created_by',
            field=cuser.fields.CurrentUserField(related_name='projectcomment_created_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='title',
            field=models.CharField(default='', max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 12, 16, 49, 126298, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='projectcomment_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='activity',
            field=models.ManyToManyField(related_name='taskcomment_activities', to='activity.Activity', blank=True),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 12, 16, 56, 718516, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='created_by',
            field=cuser.fields.CurrentUserField(related_name='taskcomment_created_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='title',
            field=models.CharField(default='', max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 12, 17, 8, 287372, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='taskcomment_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
