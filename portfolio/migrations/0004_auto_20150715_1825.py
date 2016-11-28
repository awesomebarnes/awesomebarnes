# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('portfolio', '0003_auto_20150715_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True, default=1)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, null=True, max_length=250)),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Clients',
                'ordering': ['order'],
                'verbose_name': 'Client',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True, default=1)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True, max_length=1000)),
                ('icon', models.CharField(default='fontawesome-desktop', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Services',
                'ordering': ['order'],
                'verbose_name': 'Service',
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='url',
            field=models.URLField(blank=True, null=True, max_length=250),
        ),
    ]
