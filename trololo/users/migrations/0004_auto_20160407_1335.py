# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import chi_django_base.storage
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160331_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trololouser',
            name='photo',
            field=models.ImageField(storage=chi_django_base.storage.OverwriteStorage(), upload_to=users.models.user_photo_directory_path, blank=True),
        ),
    ]
