# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 15:40
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_auto_20171019_1613'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
