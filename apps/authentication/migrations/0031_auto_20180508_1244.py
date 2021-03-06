# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0030_auto_20180508_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='swift_number',
            field=models.CharField(max_length=20),
        ),
    ]
