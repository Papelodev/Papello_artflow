from django.shortcuts import render, get_object_or_404, redirect
from apps.orders.models import Order, OrderByClient
from django.contrib import messages

def art_customization(request, idOrder):
    print(idOrder)
    pedido = get_object_or_404(Order, idOrder=idOrder)
    print(pedido)
    return render(request, 'artCustomization/artCustomization.html', {"pedido": pedido})

def envio_de_arte(request, idOrder):
    print(idOrder)
    pedido = get_object_or_404(Order, idOrder=idOrder)
    return render(request, 'artCustomization/envio_de_arte.html', {"pedido": pedido} )

def arte_enviada(request):
    messages.success(request, 'Muito Obrigado! Te avisaremos se precisarmos de mais alguma coisa')
    return render(request, 'artCustomization/teste_aviso.html')