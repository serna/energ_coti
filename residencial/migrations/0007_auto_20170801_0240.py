# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-01 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residencial', '0006_auto_20170706_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_1er_escalon', models.DecimalField(decimal_places=3, max_digits=7)),
                ('costo_2do_escalon', models.DecimalField(decimal_places=3, max_digits=7)),
                ('costo_excedente', models.DecimalField(decimal_places=3, max_digits=7)),
                ('rango_1er_escalon', models.IntegerField()),
                ('rango_2do_escalon', models.IntegerField()),
                ('cargo_fijo', models.DecimalField(decimal_places=3, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Residencial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarifa', models.CharField(max_length=2)),
                ('costo_basico', models.DecimalField(decimal_places=3, max_digits=7)),
                ('costo_intermedio', models.DecimalField(decimal_places=3, max_digits=7)),
                ('costo_excedente', models.DecimalField(decimal_places=3, max_digits=7)),
                ('costo_DAC', models.DecimalField(decimal_places=3, max_digits=7)),
                ('rango_basico', models.IntegerField()),
                ('rango_intermedio', models.IntegerField()),
                ('rango_excedente', models.IntegerField()),
                ('cargo_fijo', models.DecimalField(decimal_places=3, max_digits=7)),
            ],
        ),
        migrations.DeleteModel(
            name='Tarifa',
        ),
    ]
