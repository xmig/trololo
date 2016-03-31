# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20160329_0839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['pk']},
        ),
    ]
