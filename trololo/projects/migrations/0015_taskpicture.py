# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import projects.models
import chi_django_base.storage


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160428_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_upload', models.FileField(storage=chi_django_base.storage.OverwriteStorage(), upload_to=projects.models.task_directory_path, blank=True)),
                ('task', models.ForeignKey(related_name='files', to='projects.Task')),
            ],
        ),
    ]
