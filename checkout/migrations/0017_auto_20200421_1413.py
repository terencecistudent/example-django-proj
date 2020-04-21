# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-21 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0016_auto_20200420_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderline', to='checkout.Order'),
        ),
    ]
