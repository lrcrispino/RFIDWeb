# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180416_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlist',
            name='id',
        ),
        migrations.AddField(
            model_name='accesslog',
            name='username',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='app.userlist'),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='scan_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]