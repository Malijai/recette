# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-07 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(to='recette.Category'),
        ),
    ]
