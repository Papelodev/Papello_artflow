from django.contrib import admin
from apps.usuarios.models import MyUser

class ListandoUsuarios(admin.ModelAdmin):
    
    list_display =("id","username","is_staff","user_type")
    list_display_links=("id","username",)
    list_filter = ("user_type",)
    #list_editable = ("isActive",)
    list_per_page = 10

admin.site.register(MyUser, ListandoUsuarios)