# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal = ["groups"]
admin.site.register(Photo, PhotoAdmin)
