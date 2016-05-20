# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import chi_django_base.storage
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20160518_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskpicture',
            name='file_upload',
            field=models.FileField(storage=chi_django_base.storage.OverwriteStorage(), upload_to=projects.models.task_directory_path, blank=True),
        ),
    ]
