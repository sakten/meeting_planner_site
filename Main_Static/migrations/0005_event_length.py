# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 16:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Static', '0004_auto_20160407_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='length',
            field=models.TimeField(default=datetime.datetime(2016, 4, 7, 16, 58, 6, 616331, tzinfo=utc)),
            preserve_default=False,
        ),
    ]