from django.contrib import admin
from apps.orders.models import Order, OrderByClient

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


class listandoPedidosPorClientes(admin.ModelAdmin):
    list_display =("idOrder","name","status","registerDate")
    
admin.site.register(OrderByClient, listandoPedidosPorClientes)