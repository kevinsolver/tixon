# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-02 16:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0037_wechataccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlipayAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alipay_account', models.CharField(max_length=128, verbose_name='Alipay account')),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='wechataccount',
            name='wechat_qr',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]