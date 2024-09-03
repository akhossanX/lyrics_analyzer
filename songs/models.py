from django.db import models

class Song(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    lyrics = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    countries = models.TextField(blank=True)

    class Meta:
        unique_together = ['artist', 'title']
