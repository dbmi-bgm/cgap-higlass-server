# Generated by Django 2.1.11 on 2020-10-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tilesets', '0012_auto_20190923_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='tileset',
            name='requiresAuthentication',
            field=models.BooleanField(default=True),
        ),
    ]
