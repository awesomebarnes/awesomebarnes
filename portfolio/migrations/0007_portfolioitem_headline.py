# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-11-28 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20161128_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='headline',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
