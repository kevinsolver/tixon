# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-02 07:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0065_auto_20190531_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disputeupload',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defender_user_details', to=settings.AUTH_USER_MODEL),
        ),
    ]
