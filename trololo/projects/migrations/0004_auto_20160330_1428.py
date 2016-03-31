# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20160330_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcomment',
            name='title',
            field=models.CharField(default='', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='title',
            field=models.CharField(default='', max_length=200, null=True, blank=True),
        ),
    ]
