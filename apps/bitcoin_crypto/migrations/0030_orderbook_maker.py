# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0029_transaction_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderbook',
            name='maker',
            field=models.BooleanField(default=False),
        ),
    ]
