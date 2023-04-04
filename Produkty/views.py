from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty

# Create your views here.
def index(request):
    wszystkie = Produkty.objects.all()
    jeden = Produkty.objects.get(pk=6)
    kat = Produkty.objects.filter(kategoria=2)
    autor = Produkty.objects.filter(autor=2)
    kat_name = Kategoria.object.get(id=5)
    kategorie = Kategoria.object.all()
    null = Produkty.objects.filter(kategoria__isnull=False)
    zawiera = Produkty.objects.filter(opis__icontains='przygoda')

    return HttpResponse(kategorie)

    dane = { 'kategoria' : kategorie}
    return render(request,'szablon.html', dane)

#kontekst jest słownikiem mapującym nazwy zmiennych szablonu, template do obiektu

def kategoria (request,id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)

def produkt (request,id):
    produkt_user = Produkty.objects.get(pk=id)
    napis = "<h1>" + str(produkt_user) + "</h1>" + \
            "<p>" + str(produkt_user.opis) + "<p>" +\
            "<p>" + str(produkt_user.cena) + "<p>"
            return HttpResponse(napis)
