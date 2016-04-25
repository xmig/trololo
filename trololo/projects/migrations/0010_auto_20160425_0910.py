# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20160420_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_finished',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_started',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
