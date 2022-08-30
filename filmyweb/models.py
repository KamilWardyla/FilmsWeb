from django.db import models


class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000, blank=False)
    opis = models.TextField(default="Opis")
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    # max_digits => wszystkie cyfry, decimal_places = miejsca po przecinku
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)

    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return f"{self.tytul} ({self.rok}) ocena: {self.imdb_rating}"
