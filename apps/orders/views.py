from django.shortcuts import render, redirect, get_object_or_404

from apps.orders.models import Order, OrderProduct, Product

from apps.usuarios.models import MyUser

from apps.customers.models import CustomerProfile

from django.http import HttpResponse

import requests

from django.contrib import auth, messages
# Create your views here.

def meus_pedidos(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
    if request.user.user_type == 1:
        customer = CustomerProfile.objects.get(user=request.user)
        pedidos = Order.objects.order_by("idOrder").filter(idCustomer=customer.idCustomer)
    return render(request, 'orders/meus_pedidos.html', {"pedidos": pedidos})

def detalhe_pedido(request, idOrder):
    pedido = get_object_or_404(Order, idOrder=idOrder)
    produtos_pedido = OrderProduct.objects.filter(order=pedido)
    produtos_ids = [produto.id for produto in produtos_pedido]
    produtos_associados = Product.objects.filter(id__in=produtos_ids)
    print(produtos_associados)
    return render(request, 'orders/detalhe_pedido.html', {'pedido': pedido, 'produtos': produtos_pedido})