# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0038_auto_20180528_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermatchinghistory',
            name='trading_fee',
            field=models.FloatField(default=0),
        ),
    ]
