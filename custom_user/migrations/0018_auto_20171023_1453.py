# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0017_auto_20171023_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='postal',
        ),
    ]
