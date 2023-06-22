from django.urls import path
from artCustomization.views import art_customization

urlpatterns = [
    path('art-customization/<int:idOrder>', art_customization, name='art_customization'),
]