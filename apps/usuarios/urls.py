from django.urls import path 
from apps.usuarios.views import login, cadastro, logout, meus_dados

urlpatterns = [
    
path('login', login, name='login'),
path('cadastro', cadastro, name='cadastro'),
path('logout',logout, name='logout'),
path('meus-dados',meus_dados, name='meus_dados'),

]