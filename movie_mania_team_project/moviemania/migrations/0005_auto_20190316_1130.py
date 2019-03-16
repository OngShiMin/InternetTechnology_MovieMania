# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviemania', '0004_auto_20190316_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='watchlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlistCount_movie', to='moviemania.Movie', verbose_name='Movie'),
        ),
    ]
