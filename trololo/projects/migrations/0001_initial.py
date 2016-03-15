# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=100, null=True, blank=True)),
                ('status', models.CharField(default='undefined', max_length=30, choices=[('breakthrough', 'Breakthrough'), ('in_progress', 'In_progress'), ('finished', 'Finished'), ('undefined', 'Undefined')])),
                ('description', models.TextField(default='', max_length=1000, null=True, blank=True)),
                ('visible_by', models.CharField(default='undefined', max_length=30, choices=[('members', 'Members'), ('particular_user', 'Particular_user'), ('all_users', 'All_users'), ('undefined', 'Undefined')])),
                ('date_started', models.DateTimeField(default='', null=True, blank=True)),
                ('date_finished', models.DateTimeField(default='', null=True, blank=True)),
                ('member', models.ManyToManyField(default='', related_name='projects_added', to=settings.AUTH_USER_MODEL, blank=True)),
                ('owner', models.ForeignKey(related_name='projects_owned', default='', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(default='', null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(default='', blank=True, to='projects.Project', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default='undefined', help_text='choose status', max_length=30, choices=[('breakthrough', 'Breakthrough'), ('in_progress', 'In_progress'), ('finished', 'Finished'), ('undefined', 'Undefined')])),
                ('type', models.CharField(default='undefined', help_text='choose type', max_length=30, choices=[('bug', 'Bug'), ('feature', 'Feature'), ('undefined', 'Undefined')])),
                ('label', models.CharField(default='undefined', help_text='choose label', max_length=50, choices=[('red', 'Breakthrough'), ('orange', 'In_progress'), ('green', 'Finished'), ('undefined', 'Undefined')])),
                ('name', models.CharField(default='', max_length=150, null=True, blank=True)),
                ('description', models.TextField(default='', null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deadline_date', models.DateTimeField(default='', null=True, blank=True)),
                ('estimate_minutes', models.IntegerField(default='', null=True, blank=True)),
                ('project', models.ForeignKey(default='', blank=True, to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(default='', null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(to='projects.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
