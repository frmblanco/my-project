# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 07:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0011_auto_20171020_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='country',
        ),
    ]
