# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-14 03:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0047_confirmfiattransactions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConfirmFiatTransactions',
            new_name='ConfirmFiatTransaction',
        ),
    ]
