# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 16:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0040_tradingpairs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tradingpairs',
            new_name='Tradingpair',
        ),
    ]
