# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 16:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tilesets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tileset',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tilesets', to=settings.AUTH_USER_MODEL),
        ),
    ]