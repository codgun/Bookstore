from django.contrib import admin
from .models import Produkty, Autor, Kategoria

# Register your models here.
admin.site.register(Produkty)
admin.site.register(Autor)
admin.site.register(Kategoria)
