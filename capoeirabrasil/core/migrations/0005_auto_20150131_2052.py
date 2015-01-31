# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capoeirista',
            options={'ordering': ['name'], 'verbose_name': 'capoeirista', 'verbose_name_plural': 'capoeiristas'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date'], 'verbose_name': 'evento', 'verbose_name_plural': 'eventos'},
        ),
        migrations.AddField(
            model_name='capoeirista',
            name='nickname',
            field=models.CharField(default='indefinido', max_length=50, verbose_name='apelido'),
            preserve_default=False,
        ),
    ]
