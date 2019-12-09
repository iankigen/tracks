from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
