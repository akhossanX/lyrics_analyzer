from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Song
from .forms import SongForm


@login_required
@require_http_methods(["POST"])
def add_song(request):
    form = SongForm(request.POST)
    if form.is_valid():
        artist = form.cleaned_data['artist']
        title = form.cleaned_data['title']

        song, created = Song.get_or_create_with_cache(artist, title)

        if created or not song.lyrics:
            song.lyrics = fetch_lyrics(artist, title)
            song.summary = summarize_lyrics(song.lyrics)
            song.countries = ', '.join(extract_countries(song.lyrics))
            song.save()

        return JsonResponse({
            'id': song.id,
            'artist': song.artist,
            'title': song.title,
            'summary': song.summary,
            'countries': song.countries
        })
    else:
        # Simple error message, Need to display form.errors later
        return JsonResponse({'error': 'Invalid form data'}, status=400)


@login_required
def index(request):
    return render(request, 'songs/index.html')
