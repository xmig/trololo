# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20160413_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcomment',
            name='project',
            field=models.ForeignKey(related_name='project_comments', default='', blank=True, to='projects.Project', null=True),
        ),
    ]
