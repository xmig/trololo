# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160311_1227'),
    ]

    operations = [
        migrations.RunSQL([
            "UPDATE django_site SET domain='worddict.net:81', name='worddict.net:81' WHERE id=1;",
            "INSERT INTO django_site (id, domain, name) VALUES (2, '127.0.0.1:8000', '127.0.0.1:8000');"
        ])
    ]
