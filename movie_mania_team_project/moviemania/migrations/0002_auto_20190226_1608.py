# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-26 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviemania', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
