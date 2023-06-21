from django.urls import path
from .views import request_orders, meus_pedidos, detalhe_pedido

urlpatterns = [
    path('obter-pedido-por-cliente/', request_orders, name='request_orders'),
    path('meus-pedidos/', meus_pedidos, name='meus_pedidos'),
    path('detalhe-pedido/<int:idOrder>', detalhe_pedido, name='detalhe_pedido'),
]