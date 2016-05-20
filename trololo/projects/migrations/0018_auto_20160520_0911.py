# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20160518_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskpicture',
            name='file_upload',
            field=models.FileField(upload_to=projects.models.task_directory_path, blank=True),
        ),
    ]
