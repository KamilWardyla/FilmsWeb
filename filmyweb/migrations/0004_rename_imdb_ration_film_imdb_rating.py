# Generated by Django 4.1 on 2022-08-30 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0003_film_imdb_ration_film_opis_film_plakat_film_premiera'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='imdb_ration',
            new_name='imdb_rating',
        ),
    ]