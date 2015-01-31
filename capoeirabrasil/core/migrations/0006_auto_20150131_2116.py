# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150131_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capoeirista',
            name='graduation',
            field=models.IntegerField(max_length=3, verbose_name='gradua\xe7\xe3o', choices=[(0, 'Mestre'), (1, 'Formado'), (2, 'Formado'), (3, 'Professor'), (4, 'Instrutor')]),
        ),
    ]
