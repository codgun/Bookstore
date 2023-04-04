from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty, Kategoria
from django.template import loader

# Create your views here.
def index(request):
    wszystkie = Produkty.objects.all()
    jeden = Produkty.objects.get(pk=6)
    kat = Produkty.objects.filter(kategoria=2)
    autor = Produkty.objects.filter(autor=2)
    kat_name = Kategoria.objects.get(id=1)
    produkt_nazwa = Produkty.objects.get(id=1)
    produkty = Produkty.objects.all()
    kategorie = Kategoria.objects.all()
    null = Produkty.objects.filter(kategoria__isnull=False)
    zawiera = Produkty.objects.filter(opis__icontains='przygoda')

     #return HttpResponse(wszystkie)

    dane = { 'kategorie': kategorie}
    return render(request,'szablon.html', dane)

#kontekst jest słownikiem mapującym nazwy zmiennych szablonu, template do obiektu

def kategoria (request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
            'kategoria_produkt': kategoria_produkt,
            'kategorie': kategorie}
    return render(request, 'kategoria_produkt.html', dane)


def produkt (request,id):
    produkt_user = Produkty.objects.get(pk=id)
    # napis = "<h1>" + str(produkt_user) + "</h1>" + \
    #         "<p>" + str(produkt_user.opis) + "<p>" +\
    #         "<p>" + str(produkt_user.cena) + "<p>"
    #         return HttpResponse(napis)
    dane = {'produkt_user': produkt_user,
            'kategorie': kategoria}
    return render(request, 'produkt.html', dane)