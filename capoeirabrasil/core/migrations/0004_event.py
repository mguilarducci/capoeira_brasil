# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_capoeirista_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='t\xedtulo')),
                ('description', models.TextField(verbose_name='descri\xe7\xe3o')),
                ('date', models.DateTimeField(verbose_name='data')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('capoeirista', models.ForeignKey(to='core.Capoeirista')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
