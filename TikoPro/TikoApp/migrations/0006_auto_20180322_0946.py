# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-22 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TikoApp', '0005_auto_20180322_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(default=254720000000),
        ),
    ]