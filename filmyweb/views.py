from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Film, DodatkoweInfo
from .forms import FilmForm, DodatkoweInfoForm


# READ
def wszystkie_filmy(request):
    wszystkie = Film.objects.all()  # nazwa_modelu.objects.<ORM>
    return render(request, "filmy.html", {"filmy": wszystkie})


# CREATE
def nowy_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, request.FILES or None)
    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe_info = form_dodatkowe.save()
        film.dodatkowe = dodatkowe_info
        film.save()
        return redirect(wszystkie_filmy)
    return render(request, "film_form.html", {"form": form_film, "form_dodatkowe": form_dodatkowe})


# return HttpResponse("<h1>Kamil</h1>")

# EDIT
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    try:
        dodatkowe = DodatkoweInfo.objects.get(film=film.id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe = None
    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)
    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe_info = form_dodatkowe.save()
        film.dodatkowe = dodatkowe_info
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, "film_form.html", {"form": form_film, "form_dodatkowe": form_dodatkowe})


# DELETE
@csrf_exempt
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)
    return render(request, "potwierdz.html", {"film": film})
