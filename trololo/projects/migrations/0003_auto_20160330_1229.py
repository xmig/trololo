# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20160324_0852'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20160324_0852'),
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
            field=models.DateTimeField(default=datetime.date(2016, 3, 30), auto_now_add=True),
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
            field=models.TextField(default='', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2016, 3, 30), auto_now=True),
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
            field=models.DateTimeField(default=datetime.date(2016, 3, 30), auto_now_add=True),
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
            field=models.TextField(default='', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2016, 3, 30), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='taskcomment_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(related_name='tasks', default='', blank=True, to='projects.Project', null=True),
        ),
    ]
