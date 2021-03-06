# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=10)),
                ('residencial_basico', models.DecimalField(decimal_places=2, max_digits=7)),
                ('residencial_intermedio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('residencial_excedente', models.DecimalField(decimal_places=2, max_digits=7)),
                ('DAC', models.DecimalField(decimal_places=2, max_digits=7)),
                ('comercial_1er_escalon', models.DecimalField(decimal_places=2, max_digits=7)),
                ('comercial_2do_escalon', models.DecimalField(decimal_places=2, max_digits=7)),
                ('comercial_excedente', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
