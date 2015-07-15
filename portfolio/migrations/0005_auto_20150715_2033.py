# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminsortable.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20150715_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='icon_class',
            field=models.CharField(default='fontawesome-at', max_length=100),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='team_member',
            field=adminsortable.fields.SortableForeignKey(to='portfolio.TeamMember'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='url',
            field=models.URLField(default='http://example.com/', max_length=250),
            preserve_default=False,
        ),
    ]
