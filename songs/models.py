from django.db import models
from django.core.cache import cache

class Song(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    lyrics = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    countries = models.TextField(blank=True)

    class Meta:
        unique_together = ['artist', 'title']

    def __str__(self):
        return f"{self.artist} - {self.title}"

    @classmethod
    def get_or_create_with_cache(cls, artist, title):
        cache_key = f"song:{artist}:{title}"
        cached_song = cache.get(cache_key)

        if cached_song:
            return cached_song, False

        song, created = cls.objects.get_or_create(
            artist=artist,
            title=title
        )

        cache.set(cache_key, song, timeout=3600)  # Cache for 1 hour
        return song, created