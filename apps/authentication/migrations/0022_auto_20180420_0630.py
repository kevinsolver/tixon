# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 06:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_previouspassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='previouspassword',
            name='time',
        ),
        migrations.AlterUniqueTogether(
            name='previouspassword',
            unique_together=set([('user', 'password')]),
        ),
    ]
