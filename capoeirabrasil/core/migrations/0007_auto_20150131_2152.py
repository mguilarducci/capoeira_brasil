# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150131_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='t\xedtulo')),
                ('description', models.TextField(verbose_name='descri\xe7\xe3o', blank=True)),
                ('photo', models.ImageField(upload_to=b'event_photos')),
                ('event', models.ForeignKey(to='core.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='capoeirista',
            options={'ordering': ['nickname'], 'verbose_name': 'capoeirista', 'verbose_name_plural': 'capoeiristas'},
        ),
    ]
