from django.urls import path
from .views import meus_pedidos, detalhe_pedido, customizacao, envio_de_arte, arte_finalizada, detalhe_arte, aprova_arte, envio_prototipo, pegar_card, verifica_prototipo, aprova_prototipo

urlpatterns = [
    path('meus-pedidos/', meus_pedidos, name='meus_pedidos'),
    path('detalhe-pedido/<int:idOrder>', detalhe_pedido, name='detalhe_pedido'),
    path('customizacao/<int:idOrder>', customizacao, name='customizacao'),
    path('envio-de-arte/<int:idOrder>', envio_de_arte, name="envio_de_arte"),
    path("arte-finalizada", arte_finalizada, name="arte_finalizada"),
    path('detalhe-arte/<int:artId>', detalhe_arte, name='detalhe_arte'),
    path('aprova-arte/<int:artId>/<int:isApproved>', aprova_arte, name='aprova_arte'),
    path('detalhe-arte-aprovada/<int:artId>', detalhe_arte, name='detalhe_arte'),
    path('envio-prototipo/<int:artId>', envio_prototipo, name='envio_prototipo'),
    path('pegar-card/<int:artId>', pegar_card, name='pegar_card'),
    path('verifica-prototipo/<int:idOrder>', verifica_prototipo, name='verifica_prototipo'),
    path('aprova-prototipo/<int:artId>//<int:isApproved>', aprova_prototipo, name='aprova_prototipo'),
]