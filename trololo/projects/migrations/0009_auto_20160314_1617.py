# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20160314_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='', blank=True, to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(default='', to='projects.Task'),
        ),
    ]
