# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-21 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('gamestrike_app', '0006_auto_20190721_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 21)),
            preserve_default=False,
        ),
    ]