# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 13:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180424_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='entrydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 24, 13, 16, 10, 119668, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='entrydate',
            field=models.DateField(default=datetime.datetime(2018, 4, 24, 13, 16, 9, 711586, tzinfo=utc)),
        ),
    ]
