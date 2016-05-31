# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_task_assigned_member'),
    ]


    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status'
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(to='projects.Status', blank=True, null=True, default=''),
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['pk']},
        )
    ]


    # operations = [
    #     migrations.AlterField(
    #         model_name='task',
    #         name='status',
    #         field=models.ForeignKey(to='projects.Status', blank=True),
    #     ),
    # ]
