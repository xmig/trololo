# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160425_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_finished',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='date_started',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True),
        ),
    ]
