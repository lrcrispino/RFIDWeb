# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]