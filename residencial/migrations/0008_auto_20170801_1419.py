# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-01 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residencial', '0007_auto_20170801_0240'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipoGeneragor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('potencia', models.IntegerField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'verbose_name_plural': 'Equipos generadores',
            },
        ),
        migrations.AlterModelOptions(
            name='residencial',
            options={'verbose_name_plural': 'Servicio residencial'},
        ),
    ]