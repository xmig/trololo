# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import chi_django_base.models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=100, null=True, blank=True)),
                ('status', models.CharField(default='undefined', max_length=30, choices=[('breakthrough', 'Breakthrough'), ('in_progress', 'In_progress'), ('finished', 'Finished'), ('undefined', 'Undefined')])),
                ('description', models.TextField(default='', max_length=1000, null=True, blank=True)),
                ('visible_by', models.CharField(default='undefined', max_length=30, choices=[('members', 'Members'), ('particular_user', 'Particular_user'), ('all_users', 'All_users'), ('undefined', 'Undefined')])),
                ('date_started', models.DateTimeField(default='', null=True, blank=True)),
                ('date_finished', models.DateTimeField(default='', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, chi_django_base.models.AbstractAddOldObject),
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(default='', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=150, null=True, blank=True)),
                ('description', models.TextField(default='', null=True, blank=True)),
                ('status', models.CharField(default='undefined', help_text='choose status', max_length=30, choices=[('breakthrough', 'Breakthrough'), ('in_progress', 'In_progress'), ('finished', 'Finished'), ('undefined', 'Undefined')])),
                ('type', models.CharField(default='undefined', help_text='choose type', max_length=30, choices=[('bug', 'Bug'), ('feature', 'Feature'), ('undefined', 'Undefined')])),
                ('label', models.CharField(default='undefined', help_text='choose label', max_length=50, choices=[('red', 'Red'), ('orange', 'Orange'), ('green', 'Green'), ('undefined', 'Undefined')])),
                ('deadline_date', models.DateTimeField(default='', null=True, blank=True)),
                ('estimate_minutes', models.IntegerField(default='', null=True, blank=True)),
                ('activity', models.ManyToManyField(related_name='task_activities', to='activity.Activity', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, chi_django_base.models.AbstractAddOldObject),
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(default='', null=True, blank=True)),
                ('task', models.ForeignKey(default='', blank=True, to='projects.Task', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
