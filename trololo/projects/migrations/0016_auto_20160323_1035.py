# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20160321_1344'),
        ('projects', '0015_remove_task_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='activity',
            field=models.ManyToManyField(related_name='task_activities', null=True, to='activity.Activity', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='activity',
            field=models.ManyToManyField(related_name='project_activities', null=True, to='activity.Activity', blank=True),
        ),
    ]
