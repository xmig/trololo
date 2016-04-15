# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20160401_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(related_name='task_comments', default='', blank=True, to='projects.Task', null=True),
        ),
    ]
