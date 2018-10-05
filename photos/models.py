# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from chronos import models as chronos

# Create your models here.
class Photo(models.Model):
    src = models.URLField(null=False, verbose_name="link")
    title = models.CharField(max_length=400)
    alt = models.TextField()
    slug = models.SlugField(null=False, default="old", unique=True)

    groups = models.ManyToManyField(chronos.Album)

    def __str__(self): return self.title

    @staticmethod
    def random(count = 1):
        return Photo.objects.order_by("?")[0:count]

    def url(self):
        return "/photo/" + self.slug
