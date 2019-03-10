# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-09 10:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moviemania', '0005_auto_20190301_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=128)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
        migrations.AddField(
            model_name='movie',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='comments',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviemania.Movie'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
