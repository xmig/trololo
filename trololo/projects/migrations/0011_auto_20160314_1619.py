# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160314_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(default='', blank=True, to='projects.Task', null=True),
        ),
    ]
