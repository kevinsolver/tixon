# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-14 03:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bitcoin_crypto', '0046_auto_20181213_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmFiatTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('fiat_type', models.CharField(max_length=5)),
                ('receive_address', models.CharField(max_length=128)),
                ('is_confirm', models.BooleanField(default=False)),
                ('sender', models.CharField(max_length=128)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
