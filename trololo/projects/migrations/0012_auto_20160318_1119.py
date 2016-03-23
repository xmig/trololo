# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_activity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='member',
            new_name='members',
        ),
    ]
