# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20160314_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='task',
            field=models.ForeignKey(default='', blank=True, to='projects.Task'),
        ),
    ]
