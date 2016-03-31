# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160325_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trololouser',
            options={'ordering': ['id']},
        ),
    ]
