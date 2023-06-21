from django.contrib import admin
from apps.orders.models import Order, OrderByClient

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =("idQueue","idOrder","nameStatus", "idCustomer")
    list_per_page = 15
    search_fields = ("idOrder",)

class listandoPedidosPorClientes(admin.ModelAdmin):
    list_display =("idOrder","name","status","registerDate")
    
admin.site.register(OrderByClient, listandoPedidosPorClientes)