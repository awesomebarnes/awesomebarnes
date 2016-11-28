# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminsortable.fields
import autoslug.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('order', models.PositiveIntegerField(default=1, db_index=True, editable=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, null=True, max_length=250)),
                ('icon_class', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Social link',
                'abstract': False,
                'verbose_name_plural': 'Social links',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('order', models.PositiveIntegerField(default=1, db_index=True, editable=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('name', models.CharField(max_length=50)),
                ('caption', models.CharField(blank=True, null=True, max_length=250)),
                ('description', models.TextField(blank=True, null=True, max_length=1000)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', null=True, blank=True)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Team member',
                'abstract': False,
                'verbose_name_plural': 'Team members',
            },
        ),
        migrations.AlterModelOptions(
            name='portfolioitem',
            options={'verbose_name_plural': 'Portfolio items', 'ordering': ['order'], 'verbose_name': 'Portfolio item'},
        ),
        migrations.AddField(
            model_name='sociallink',
            name='team_member',
            field=adminsortable.fields.SortableForeignKey(to='portfolio.TeamMember', null=True, blank=True),
        ),
    ]
