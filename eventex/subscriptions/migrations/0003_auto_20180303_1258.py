# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-03 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20180303_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='pago'),
        ),
    ]
