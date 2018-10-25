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
    get_absolute_url = url

    @property
    def starts(self):
        try:
            return max(group.start for group in self.groups.all())
        except ValueError:
            return None
    @property
    def ends(self):
        try:
            return min(group.end for group in self.groups.all())
        except ValueError:
            return None

    def date(self):
        def optional(item): return "?" if item is None else str(item)
        return optional(self.starts) + " – " + optional(self.ends)

def propagate_dates():
    made_changes = True
    while made_changes:
        made_changes = False
        for photo in Photo.objects.all():
            if photo.starts is None and photo.ends is None: continue

            if photo.starts is not None:
                for group in photo.groups:
                    # TODO Communicate the computer made these changes.
                    if group.start is None or group.start > photo.starts:
                        group.date("Date propagation", photo.starts,
                                reference=photo.url())
                        made_changes = True
            if photo.ends is not None:
                for group in photo.groups:
                    # TODO Communicate the computer made these changes.
                    if group.end is None or group.end < photo.ends:
                        group.date("Date propagation", end=photo.ends,
                                reference=photo.url())
                        group.save()
                        made_changes = True
