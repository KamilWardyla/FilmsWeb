from django.shortcuts import render
from django.http import HttpResponse
from .models import Film


def wszystkie_filmy(request):
    wszystkie = Film.objects.all() #nazwa_modelu.objects.<ORM>
    return render(request, "filmy.html", {"filmy": wszystkie})
# return HttpResponse("<h1>Kamil</h1>")
