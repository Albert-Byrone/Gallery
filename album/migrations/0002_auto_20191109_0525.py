# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-09 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
