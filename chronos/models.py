from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=400, null=False)
    description = models.TextField(null=True)
    href = models.URLField(null=True)

    start = models.DateField(null=True)
    end = models.DateField(null=True)
