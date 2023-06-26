from django.urls import path
from artCustomization.views import art_customization, envio_de_arte, arte_enviada, arte_finalizada

urlpatterns = [
    path('art-customization/<int:idOrder>', art_customization, name='art_customization'),
    path('envio-de-arte/<int:idOrder>', envio_de_arte, name="envio_de_arte"),
    path("arte-enviada", arte_enviada, name="arte_enviada"),
    path("arte-finalizada", arte_finalizada, name="arte_finalizada"),
]