# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-30 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20180829_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanners',
            name='area',
            field=models.CharField(default='default', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scanners',
            name='direction',
            field=models.CharField(choices=[('in', 'In'), ('out', 'Out')], default='in', max_length=3),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='status',
            field=models.CharField(choices=[('in', 'In'), ('out', 'Out')], default='in', max_length=3),
        ),
    ]