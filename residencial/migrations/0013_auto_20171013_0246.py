# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-13 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residencial', '0012_auto_20171013_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='IVA',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='indirectos',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='utilidad',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]