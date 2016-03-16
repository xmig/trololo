# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractSignable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_by', cuser.fields.CurrentUserField(related_name='created_by', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', cuser.fields.CurrentUserField(related_name='updated_by', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
