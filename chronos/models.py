# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=400, null=False)
    description = models.TextField(null=True, blank=True)
    href = models.URLField(null=True, blank=True, verbose_name="link")
    slug = models.SlugField(null=False, default="old", unique=True)

    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def date(self):
        def optional(item): return "?" if item is None else str(item)
        return optional(self.start) + " – " + optional(self.end)
