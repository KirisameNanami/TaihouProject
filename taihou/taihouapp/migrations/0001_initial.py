# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('AccountName', models.CharField(max_length=256, verbose_name='Account')),
                ('Passwd', models.CharField(max_length=256, verbose_name='Password')),
                ('RegisterTime', models.DateTimeField(auto_now_add=True, verbose_name='RegisterTime')),
            ],
        ),
    ]
