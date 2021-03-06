# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-12 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residencial', '0008_auto_20170801_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proovedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proovedor', models.CharField(max_length=20)),
                ('contacto', models.CharField(max_length=50)),
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
        ),
        migrations.RenameModel(
            old_name='EquipoGeneragor',
            new_name='EquipoGenerador',
        ),
    ]
