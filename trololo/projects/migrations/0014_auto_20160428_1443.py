# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20160428_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='estimate_minutes',
            field=models.IntegerField(default=172800, null=True, blank=True),
        ),
    ]
