# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160314_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='', blank=True, to='projects.Project'),
        ),
    ]
