# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0039_ordermatchinghistory_trading_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tradingpairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradingpairs', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
    ]
