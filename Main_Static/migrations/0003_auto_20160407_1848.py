# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Static', '0002_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='particip_events',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
