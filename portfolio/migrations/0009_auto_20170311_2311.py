# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-11 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_privacypolicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacypolicy',
            name='html',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
