# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-29 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_scanners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scanners',
            name='id',
        ),
        migrations.AlterField(
            model_name='scanners',
            name='clientid',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
