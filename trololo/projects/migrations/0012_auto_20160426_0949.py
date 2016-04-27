# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20160425_1518'),
    ]

    operations = [
        migrations.RunSQL("DELETE FROM projects_status WHERE project_id is null;"),
        migrations.AlterField(
            model_name='status',
            name='project',
            field=models.ForeignKey(related_name='project_statuses', blank=True, to='projects.Project'),
        ),
    ]
