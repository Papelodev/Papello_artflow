from django.contrib import admin
from apps.galeria.models import Fotografia, Arte

class ListandoFotografias(admin.ModelAdmin):
    list_display =("id","nome","legenda","publicada")
    list_display_links =("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria","usuario",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)

class ListandoArtes(admin.ModelAdmin):
    list_display =('idCustomer', 'idOrder', 'status', 'idProduct')
    list_display_links =("idCustomer","idOrder")
    search_fields = ("idOrder",)

    list_per_page = 10

admin.site.register(Arte, ListandoArtes)
