# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-02 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0066_auto_20190602_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='disputeupload',
            name='dispute_status',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]