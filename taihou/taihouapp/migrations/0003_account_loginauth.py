# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taihouapp', '0002_remove_account_passwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='LoginAuth',
            field=models.BooleanField(default=False),
        ),
    ]
