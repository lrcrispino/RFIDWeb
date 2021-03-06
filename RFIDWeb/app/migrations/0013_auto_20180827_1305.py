# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-27 17:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180424_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='entrydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 27, 17, 5, 33, 687576, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='username',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.SET_DEFAULT, to='app.userlist'),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='entrydate',
            field=models.DateField(default=datetime.datetime(2018, 8, 27, 17, 5, 33, 686575, tzinfo=utc)),
        ),
    ]
