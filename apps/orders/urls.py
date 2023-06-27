from django.urls import path
from .views import meus_pedidos, detalhe_pedido

urlpatterns = [
    path('meus-pedidos/', meus_pedidos, name='meus_pedidos'),
    path('detalhe-pedido/<int:idOrder>', detalhe_pedido, name='detalhe_pedido'),
]