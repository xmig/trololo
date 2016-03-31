# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20160331_1029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['-order_number', 'pk']},
        ),
    ]
