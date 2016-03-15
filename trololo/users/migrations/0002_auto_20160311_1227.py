# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trololouser',
            name='department',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='trololouser',
            name='detailed_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='trololouser',
            name='photo',
            field=models.ImageField(upload_to=users.models.user_photo_directory_path, blank=True),
        ),
        migrations.AlterField(
            model_name='trololouser',
            name='specialization',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
