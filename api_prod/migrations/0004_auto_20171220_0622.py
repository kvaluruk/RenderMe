# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_prod', '0003_auto_20171218_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humanoidapi',
            name='age',
            field=models.FloatField(default=25),
        ),
        migrations.AlterField(
            model_name='humanoidapi',
            name='weight_kg',
            field=models.FloatField(default=60),
        ),
    ]
