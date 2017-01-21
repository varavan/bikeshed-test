# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('mountain', 'Mountain'), ('road', 'Road'), ('hybrid', 'Hybrid')], max_length=10)),
                ('created_at', models.DateTimeField()),
                ('model', models.CharField(max_length=255)),
                ('headline', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('size', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Brand'),
        ),
    ]
