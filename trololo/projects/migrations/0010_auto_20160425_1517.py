# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20160420_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date_finished',
        ),
        migrations.RemoveField(
            model_name='project',
            name='date_started',
        ),
    ]
