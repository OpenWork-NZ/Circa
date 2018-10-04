from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=400, null=False)
    description = models.TextField(null=True, blank=True)
    href = models.URLField(null=True, blank=True)
    slug = AutoSlugField(null=False, default="old", unique=True, populate_from="title")

    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
