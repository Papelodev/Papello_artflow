from django.urls import path
from artCustomization.views import art_customization, envio_de_arte

urlpatterns = [
    path('art-customization/<int:idOrder>', art_customization, name='art_customization'),
    path('envio-de-arte/<int:idOrder>', envio_de_arte, name="envio_de_arte")
]