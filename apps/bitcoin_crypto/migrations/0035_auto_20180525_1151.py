# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0034_tradedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradedetails',
            name='site',
        ),
        migrations.AddField(
            model_name='orderbook',
            name='maker',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='TradeDetails',
        ),
    ]
