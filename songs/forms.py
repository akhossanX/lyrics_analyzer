from django import forms

class SongForm(forms.Form):
    artist = forms.CharField(max_length=100, required=True)
    title = forms.CharField(max_length=100, required=True)