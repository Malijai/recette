# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-07 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0003_auto_20171107_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quantite',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recette',
            name='quantite',
            field=models.ManyToManyField(to='recette.Quantite'),
        ),
    ]