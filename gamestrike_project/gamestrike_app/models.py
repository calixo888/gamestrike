# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.db import models
from django.contrib.auth.models import User
from gamestrike_project.settings import MEDIA_DIR
# Create your models here.

User._meta.get_field('email')._unique = True

def path_and_rename(instance, filename):
    upload_to = 'profile_pictures'
    ext = filename.split('.')[-1]
    if not ext == "png":
        ext = "png"
    filename = '{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)
    os.remove("../media/profile_pictures/{}".format(filename))

class Game(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    image_url = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=130)
    instructions = models.TextField()
    points = models.IntegerField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)
    profile_picture = models.ImageField(upload_to=path_and_rename, blank=True, default="default.png")

    def __str__(self):
        return self.user.username
