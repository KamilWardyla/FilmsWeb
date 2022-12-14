from django.db import models


# ONE TO ONE
class DodatkoweInfo(models.Model):
    GATUNEK = {
        (0, "Inne"),
        (1, "Horror"),
        (2, "Komedia"),
        (3, "Sci-Fi"),
        (4, "Dramat"),
        (5, "Fantasy"),
        (6, "Animacja"),
        (7, "Biograficzny"),
    }
    czas_trwania = models.PositiveIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)


class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000, blank=False)
    opis = models.TextField(default="Opis")
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    # max_digits => wszystkie cyfry, decimal_places = miejsca po przecinku
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    dodatkowe_info = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return f"{self.tytul} ({self.rok}) ocena: {self.imdb_rating}"


# MANY TO ONE
class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


# MANY TO MANY
class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film)
