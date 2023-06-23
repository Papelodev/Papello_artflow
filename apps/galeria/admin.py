from django.contrib import admin
from apps.galeria.models import Fotografia
from apps.galeria.models import Artes

class ListandoFotografias(admin.ModelAdmin):
    list_display =("id","nome","legenda","publicada")
    list_display_links =("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria","usuario",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)

class ListandoArtes(admin.ModelAdmin):
    list_display =("idCustomer",)
    list_display_links =("idCustomer",)
    search_fields = ("idCustomer",)
    list_per_page = 10

admin.site.register(Artes, ListandoArtes)
