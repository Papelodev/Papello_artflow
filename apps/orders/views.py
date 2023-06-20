from django.shortcuts import render

from apps.orders.models import Order, OrderByClient

from django.http import HttpResponse

import requests

def request_orders(request):
    url = 'http://localhost:3001/orders'

    params = {
        'email': 'coalacookies@gmail.com',
        'cpfCnpj': 39653162000164,
    }

    response = requests.get(url, params)
    
    if response.status_code == 200:
        dados = response.json()
        print(dados[0])

        order_by_client = OrderByClient(
            idOrder=dados[0]['idOrder'],
            status=dados[0]['status'],
            total=dados[0]['total'],
            totalItems=dados[0]['totalItems'],
            totalDiscount=dados[0]['totalDiscount'],
            quantityItems=dados[0]['quantityItems'],
            document=dados[0]['document'],
            name=dados[0]['name'],
    )

        order_by_client.save()

        return HttpResponse('Dados da API obtidos com sucesso!')
    else:
        return HttpResponse('Falha ao obter dados da API')


def request_all_orders(request):
        url = 'http://localhost:3001/'

        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            print(dados[0])

            order = Order(
            idQueue = dados[0]['idQueue'],
            idOrder=dados[0]['entity'],
            status=dados[0]['status'],
            total=dados[0]['total'],
            totalItems=dados[0]['totalItems'],
            totalDiscount=dados[0]['totalDiscount'],
            quantityItems=dados[0]['quantityItems'],
            document=dados[0]['document'],
            name=dados[0]['name'],
    )
            order.save()

            return HttpResponse('Dados da API obtidos com sucesso!')
        else:
            return HttpResponse('Falha ao obter dados da API')