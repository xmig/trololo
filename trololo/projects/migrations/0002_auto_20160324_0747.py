# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20160324_0747'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_by',
            field=cuser.fields.CurrentUserField(related_name='task_created_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='members',
            field=models.ManyToManyField(related_name='tasks_added', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='', blank=True, to='projects.Project', null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='task_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='project',
            field=models.ForeignKey(default='', blank=True, to='projects.Project', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='activity',
            field=models.ManyToManyField(related_name='project_activities', to='activity.Activity', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=cuser.fields.CurrentUserField(related_name='project_created_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projects_added', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='project_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
