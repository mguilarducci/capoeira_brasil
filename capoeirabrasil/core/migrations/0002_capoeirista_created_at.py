# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capoeirista',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2015, 1, 31), verbose_name='criado em', auto_now_add=True),
            preserve_default=False,
        ),
    ]
