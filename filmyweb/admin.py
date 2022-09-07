from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Aktor


# Register your models here.
# admin.site.register(Film) <= better
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """fields = ["tytul", "opis", "rok"]
      exclude = ["opis"]"""
    list_display = ["tytul", "rok", "imdb_rating"]
    list_filter = ["tytul", "rok"]
    search_fields = ["tytul"]


admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)
