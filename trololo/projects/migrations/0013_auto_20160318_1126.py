# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20160318_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='member',
            new_name='members',
        ),
    ]
