# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-04 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'jugador')),
            ],
            options={
                'verbose_name': 'jugador',
                'verbose_name_plural': 'jugadores',
            },
        ),
    ]
