# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160324_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('order_number', models.IntegerField()),
                ('project', models.ForeignKey(related_name='project_statuses', default=True, blank=True, to='projects.Project', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(related_name='tasks', default='', blank=True, to='projects.Project', null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='group',
            field=models.ForeignKey(related_name='task_statuses', blank=True, to='projects.Status', null=True),
        ),
    ]
