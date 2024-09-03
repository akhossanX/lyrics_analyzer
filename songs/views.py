from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Song
from .forms import SongForm
from .services import fetch_lyrics, summarize_lyrics, extract_countries

from django.shortcuts import render

from .utils import is_admin_user


@login_required
@require_http_methods(["POST"])
def add_song(request):
    if not is_admin_user(request.user):
        return JsonResponse({"error": f"{request.user.username} is required to be an Admin"})

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
