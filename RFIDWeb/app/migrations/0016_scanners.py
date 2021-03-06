# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-29 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20180827_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='scanners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientid', models.CharField(max_length=30)),
                ('door', models.CharField(max_length=30)),
                ('direction', models.CharField(max_length=30)),
                ('latch', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=30)),
                ('online', models.BooleanField(default=False)),
            ],
        ),
    ]
