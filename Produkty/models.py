from django.db import models

# Create your models here.
class Autor(models.Model):
    def __str__(self):
        return self.nazwisko

    nazwisko = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autorzy'

class Kategoria(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'


class Produkty(models.Model):
    def __str__(self):
        return self.nazwa

    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=150)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=99999,decimal_places=2)

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

