# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residencial', '0002_auto_20170706_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarifa',
            name='DAC',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='comercial_1er_escalon',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='comercial_2do_escalon',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='comercial_cargo_fijo',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='comercial_excedente',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='residencial_basico',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='residencial_cargo_fijo',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='residencial_excedente',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='residencial_intermedio',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]