# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-09 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20191109_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]