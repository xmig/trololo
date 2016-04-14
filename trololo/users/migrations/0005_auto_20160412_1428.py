# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160407_1335'),
    ]

    operations = [
        migrations.RunSQL([
            "INSERT INTO django_site (id, domain, name) VALUES (4, 'localhost:8000', 'localhost:8000');",
            "ALTER SEQUENCE django_site_id_seq RESTART WITH 5;",
        ])
    ]
