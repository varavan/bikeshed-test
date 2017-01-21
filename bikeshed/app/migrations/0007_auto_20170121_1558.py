# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 15:58
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170121_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='image_big',
        ),
        migrations.RemoveField(
            model_name='bike',
            name='image_small',
        ),
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=django_resized.forms.ResizedImageField(default='', upload_to='bike_big'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='image_thumbnail',
            field=django_resized.forms.ResizedImageField(default='', upload_to='bike_small'),
        ),
    ]
