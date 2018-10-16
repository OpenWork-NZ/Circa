# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=400, null=False)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=False, default="old", unique=True)

    @property
    def start(self):
        return self.dating_set.order('-changed_at')[0].start
    @property
    def end(self):
        return self.dating_set.order('-changed_at')[0].end

    def date(self, commitmsg, start=False, end=False, user=None, reference=None):
        if start is False: start = self.start
        if end is False: end = self.end
        Dating(changed_by=user, justification=commitmsg, reference=reference,
                start=start, end=end, for_album=self).save()

    def __str__(self):
        return self.title

    def date(self):
        def optional(item): return "?" if item is None else str(item)
        return optional(self.start) + " – " + optional(self.end)

    def get_absolute_url(self):
        return "/group/" + self.slug

class Dating(models.Model):
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    changed_at = models.DateField(auto_now=True, null=False)
    justification = models.TextField(null=False)
    reference = models.URLField(null=True, blank=True)

    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    for_album = models.ForeignKey(Album, null=False)
