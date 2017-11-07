# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-12 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residencial', '0009_auto_20171012_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('panel', models.DecimalField(decimal_places=2, max_digits=7)),
                ('conector_hembra_APS', models.DecimalField(decimal_places=2, max_digits=7)),
                ('protective_end_cap', models.DecimalField(decimal_places=2, max_digits=7)),
                ('midClamp', models.DecimalField(decimal_places=2, max_digits=7)),
                ('endClamp', models.DecimalField(decimal_places=2, max_digits=7)),
                ('base_triangular', models.DecimalField(decimal_places=2, max_digits=7)),
                ('metro_riel', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cable', models.DecimalField(decimal_places=2, max_digits=7)),
                ('medidor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('caja_registro', models.DecimalField(decimal_places=2, max_digits=7)),
                ('interruptor', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name_plural': 'Costos de instalacion',
            },
        ),
        migrations.AlterModelOptions(
            name='equipogenerador',
            options={'verbose_name_plural': 'Inversores'},
        ),
        migrations.AlterModelOptions(
            name='proovedor',
            options={'verbose_name_plural': 'Proovedores'},
        ),
        migrations.AlterModelOptions(
            name='residencial',
            options={'verbose_name_plural': 'Tarifas'},
        ),
    ]