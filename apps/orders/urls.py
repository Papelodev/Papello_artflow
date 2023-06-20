from django.urls import path
from .views import request_orders, request_all_orders

urlpatterns = [
    path('obter-pedido-por-cliente/', request_orders, name='request_orders'),
    path('obter-todos-pedidos/', request_all_orders, name='request_all_orders')
]