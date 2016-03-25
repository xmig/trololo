# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL([
            "UPDATE django_site SET domain='worddict.net:81', name='worddict.net:81' WHERE id=1;",
            "INSERT INTO django_site (id, domain, name) VALUES (2, '127.0.0.1:8000', '127.0.0.1:8000');",
            "INSERT INTO django_site (id, domain, name) VALUES (3, 'worddict.net:82', 'worddict.net:82');",
            "ALTER SEQUENCE django_site_id_seq RESTART WITH 4;",
        ])
    ]
