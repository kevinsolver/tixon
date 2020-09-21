# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0026_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationuser',
            name='is_pending_notification',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]