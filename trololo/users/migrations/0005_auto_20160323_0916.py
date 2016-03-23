# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_trololouser_get_gravatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trololouser',
            old_name='get_gravatar',
            new_name='use_gravatar',
        ),
    ]
