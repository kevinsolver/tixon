# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-02 13:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0018_auto_20180402_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderbook',
            name='coins_received',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orderbook',
            name='order_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 4, 2, 18, 10, 25, 649995)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderbook',
            name='trade_status',
            field=models.BooleanField(default=False),
        ),
    ]