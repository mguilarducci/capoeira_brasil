# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capoeirista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('phone', models.CharField(max_length=30, verbose_name='telefone')),
                ('email', models.EmailField(max_length=75, verbose_name='email', blank=True)),
                ('graduation', models.CharField(max_length=3, verbose_name='gradua\xe7\xe3o', choices=[(b'ME', 'Mestre'), (b'FP', 'Formado (Preta)'), (b'FM', 'Formado (Marrom)'), (b'PVR', 'Professor (Verde e Roxa)'), (b'IA', 'Instrutor (Azul)')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
