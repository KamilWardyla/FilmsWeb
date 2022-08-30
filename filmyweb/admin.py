from django.contrib import admin
from .models import Film


# Register your models here.
# admin.site.register(Film) <= better
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """fields = ["tytul", "opis", "rok"]
      exclude = ["opis"]"""
    list_display = ["tytul", "rok", "imdb_rating"]
    list_filter = ["tytul", "rok"]
    search_fields = ["tytul"]









