# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='postal_code',
            field=models.IntegerField(blank=True),
        ),
    ]
