# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-17 09:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_crypto', '0053_confirmfiattransaction_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmfiattransaction',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='confirmfiattransaction',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]