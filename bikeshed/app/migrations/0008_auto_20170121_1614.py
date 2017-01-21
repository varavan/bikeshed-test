# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 16:14
from __future__ import unicode_literals

import app.helpers
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170121_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=django_resized.forms.ResizedImageField(default='', upload_to=app.helpers.sanitaze_image_upload_path),
        ),
        migrations.AlterField(
            model_name='bike',
            name='image_thumbnail',
            field=django_resized.forms.ResizedImageField(default='', upload_to=app.helpers.sanitaze_image_upload_path),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=django_resized.forms.ResizedImageField(default='', upload_to=app.helpers.sanitaze_image_upload_path),
        ),
    ]