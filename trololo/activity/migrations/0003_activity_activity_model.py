# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20160324_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_model',
            field=models.CharField(default='project', max_length=30),
            preserve_default=False,
        ),
    ]
