# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0031_auto_20180508_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='bank_name',
            field=models.CharField(default='ABC Bank', max_length=128, verbose_name='Bank Name'),
            preserve_default=False,
        ),
    ]
