from django.contrib import admin
from apps.usuarios.models import MyUser


class ListandoUsuarios(admin.ModelAdmin):
    list_display =("username","idCustomer","cpf_cnpj")
    list_display_links =("username","idCustomer")
    search_fields = ("username",)
    list_per_page = 10

admin.site.register(MyUser, ListandoUsuarios)