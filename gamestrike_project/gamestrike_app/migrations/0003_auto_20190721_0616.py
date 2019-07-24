# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-21 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestrike_app', '0002_auto_20190721_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default='Enter Description', max_length=130),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='image_url',
            field=models.CharField(default='f', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='instructions',
            field=models.TextField(default='Enter Instructions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='type',
            field=models.CharField(default="Type", max_length=128),
            preserve_default=False,
        ),
    ]