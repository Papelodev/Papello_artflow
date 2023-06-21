from django.shortcuts import render, get_object_or_404

from apps.orders.models import Order, OrderByClient

from django.http import HttpResponse

import requests

def request_orders(request):
    url = 'http://localhost:3001/orders'

    params = {
        'email': 'comercial@seudocepramim.com.br',
        'cpfCnpj': 45752803000130,
    }

    response = requests.get(url, params)

    if response.status_code == 200: 
        dados = response.json()
        print(dados)

        for dado in dados:
            order_by_client = OrderByClient(
                idOrder=dado['idOrder'],
                status=dado['status'],
                total=dado['total'],
                totalItems=dado['totalItems'],
                totalDiscount=dado['totalDiscount'],
                quantityItems=dado['quantityItems'],
                document=dado['document'],
                name=dado['name']
            )
            order_by_client.save()

        return HttpResponse('Dados da API obtidos com sucesso!')
    else:
        return HttpResponse('Falha ao obter dados da API')


def meus_pedidos(request):
    pedidos = Order.objects.order_by("idOrder")

    print(pedidos)
    return render(request, 'orders/meus_pedidos.html', {"pedidos": pedidos})

def detalhe_pedido(request, idOrder):
    pedido = get_object_or_404(Order, idOrder=idOrder)

    return render(request, 'orders/detalhe_pedido.html', {'pedido': pedido})