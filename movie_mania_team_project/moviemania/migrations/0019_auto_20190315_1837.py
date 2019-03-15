# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-15 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviemania', '0018_auto_20190315_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='likes_movie', to='moviemania.Movie'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchlistCount_movie', to='moviemania.Movie'),
        ),
    ]