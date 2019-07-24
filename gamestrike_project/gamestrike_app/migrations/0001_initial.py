# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-21 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('image_url', models.CharField(max_length=5000)),
                ('description', models.TextField(max_length=130)),
                ('instructions', models.TextField()),
                ('points', models.IntegerField()),
            ],
        ),
    ]
