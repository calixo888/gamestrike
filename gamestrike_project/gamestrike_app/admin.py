# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from gamestrike_app.models import Game, UserProfile
# Register your models here.

admin.site.register(Game)
admin.site.register(UserProfile)
