# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20160321_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created_by',
            field=cuser.fields.CurrentUserField(related_name='activity_created_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='updated_by',
            field=cuser.fields.CurrentUserField(related_name='activity_updated_by', default=b'', editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
