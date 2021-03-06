# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-28 15:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0036_paypalaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='WechatAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wechat_account', models.CharField(max_length=128, verbose_name='Wechat account')),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
