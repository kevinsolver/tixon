# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0035_auto_20180525_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMatchingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('order_matching_time', models.DateTimeField(auto_now_add=True)),
                ('matched_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taker_order', to='bitcoin_crypto.OrderBook')),
                ('processing_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maker_oder', to='bitcoin_crypto.OrderBook')),
            ],
        ),
    ]