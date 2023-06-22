from django.shortcuts import render, get_object_or_404
from apps.orders.models import Order, OrderByClient

def art_customization(request, idOrder):
    print(idOrder)
    pedido = get_object_or_404(Order, idOrder=idOrder)
    print(pedido)
    return render(request, 'artCustomization/artCustomization.html', {"pedido": pedido})
# Create your views here.
