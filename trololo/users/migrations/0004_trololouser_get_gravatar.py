# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160316_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='trololouser',
            name='get_gravatar',
            field=models.BooleanField(default=False),
        ),
    ]
