from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm


# READ
def wszystkie_filmy(request):
    wszystkie = Film.objects.all()  # nazwa_modelu.objects.<ORM>
    return render(request, "filmy.html", {"filmy": wszystkie})


# CREATE
def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, "film_form.html", {"form": form})


# return HttpResponse("<h1>Kamil</h1>")

# EDIT
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, "film_form.html", {"form": form})

#DELETE
@csrf_exempt
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)
    return render(request, "potwierdz.html", {"film": film})
