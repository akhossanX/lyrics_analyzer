import openai
from django.conf import settings
from django.core.cache import cache

# TODO: Implement actual logic


def fetch_lyrics(artist, title):
    """
    Fetch song's lyrics from Musixmatch Developer AP
    """
    return f"These are dumb lyrics for {artist} - {title}."


def summarize_lyrics(lyrics):
    """
    Summarizes the lyrics in one sentence using  OpenAI GPT API
    """
    return f"Dummy summary"


def extract_countries(lyrics):
    """
    Returns the list of countries mentioned in the lyrics with the help of  OpenAI GPT API
    """
    return []
