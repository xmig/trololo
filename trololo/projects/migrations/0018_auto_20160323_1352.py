# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20160323_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='label',
            field=models.CharField(default='undefined', help_text='choose label', max_length=50, choices=[('red', 'Red'), ('orange', 'Orange'), ('green', 'Green'), ('undefined', 'Undefined')]),
        ),
    ]
