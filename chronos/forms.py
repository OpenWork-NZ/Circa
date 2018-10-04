from django import forms
from models import *

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "description", "href", "start", "end"]
