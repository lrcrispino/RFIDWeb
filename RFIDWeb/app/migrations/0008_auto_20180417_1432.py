# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180417_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='area',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='userlist',
            name='status',
            field=models.CharField(default='out', max_length=30),
        ),
    ]