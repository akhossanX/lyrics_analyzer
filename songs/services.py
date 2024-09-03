import openai
from django.conf import settings
import requests
from django.core.cache import cache
from django.utils.http import urlencode
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=settings.OPENAI_API_KEY,
)


def fetch_lyrics(artist, title):
    """
    Fetch song's lyrics from Musixmatch Developer API
    :param artist: The artist of the song.
    :param title: The title of the song.
    :return: The lyrics of the song, or an error message.
    """

    base_url = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get"

    # Construct the query parameters
    params = {
        'q_track': title,
        'q_artist': artist,
        'apikey': settings.MUSIXMATCH_API_KEY,
    }

    # URL encode the parameters and create the final URL
    query_url = f"{base_url}?{urlencode(params)}"

    try:
        # Send GET request to the Musixmatch API
        response = requests.get(query_url)
        data = response.json()

        # Check if lyrics are found
        status_code = data["message"]["header"]["status_code"]
        if status_code == 404:
            raise Exception("track not found")
        elif status_code == 200:
            lyrics = data["message"]["body"]["lyrics"]["lyrics_body"]
            return lyrics
        else:
            raise Exception(f"""
            couldn't get lyrics from the server: errcode={data['message']['header']['status_code']}
            """)

    except Exception as e:
        raise e


def summarize_lyrics(lyrics):
    """
    Summarizes the lyrics in one sentence using  OpenAI GPT API
    """
    cache_key = f"summary:{hash(lyrics)}"
    cached_summary = cache.get(cache_key)

    if cached_summary:
        return cached_summary

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes song lyrics."},
                {"role": "user", "content": f"Summarize these lyrics in one sentence (less than 30 words): {lyrics}"}
            ],
            model="gpt-3.5-turbo",
        )

        summary = response.choices[0].message.content.strip()
        cache.set(cache_key, summary, timeout=86400)  # Cache for 24 hours
        return summary
    except Exception as e:
        raise e


def extract_countries(lyrics):
    """
    Returns the list of countries mentioned in the lyrics with the help of  OpenAI GPT API
    """
    cache_key = f"countries:{hash(lyrics)}"
    cached_countries = cache.get(cache_key)

    if cached_countries:
        return cached_countries

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts country names from text."},
                {"role": "user", "content": f"Extract and list all country names mentioned in this text: {lyrics}"}
            ]
        )
        countries = response.choices[0].message.content.strip().split(', ')
        cache.set(cache_key, countries, timeout=86400)  # Cache for 24 hours
        return countries
    except Exception as e:
        raise e
