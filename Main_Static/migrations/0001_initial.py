# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 15:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
                ('hidden_index', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Event_description',
            },
        ),
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_work', models.TimeField()),
                ('finish_work', models.TimeField()),
                ('birth', models.DateField()),
                ('test', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]