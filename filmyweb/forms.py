from django.forms import ModelForm
from .models import Film, DodatkoweInfo


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ["tytul", "rok", "opis", "premiera", "imdb_rating", "plakat"]


class DodatkoweInfoForm(ModelForm):
    class Meta:
        model = DodatkoweInfo
        fields = ["czas_trwania", "gatunek"]
