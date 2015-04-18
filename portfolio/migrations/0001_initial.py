# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=1, db_index=True, editable=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('name', models.CharField(max_length=50)),
                ('caption', models.CharField(max_length=250, null=True, blank=True)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('image', filer.fields.image.FilerImageField(null=True, to='filer.Image', blank=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
        ),
    ]
