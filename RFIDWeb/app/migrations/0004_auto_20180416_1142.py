# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180416_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='entrydate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]