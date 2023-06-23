from django.shortcuts import render, get_object_or_404, redirect
from apps.orders.models import Order, OrderByClient
from apps.galeria.forms import ArteForms
from apps.galeria.models import Artes
from django.contrib import messages

def art_customization(request, idOrder):
    print(idOrder)
    pedido = get_object_or_404(Order, idOrder=idOrder)
    print(pedido)
    return render(request, 'artCustomization/artCustomization.html', {"pedido": pedido})

def envio_de_arte(request, idOrder):
    print(idOrder)
    pedido = get_object_or_404(Order, idOrder=idOrder)
    if request.method =='POST':
        form = ArteForms(request.POST, request.FILES)
        if form.is_valid():
            descricao = request.POST.get('descricao')
            foto = request.FILES.get('foto')
            idCustomer = request.POST.get('idCustomer')
            arte = Artes(descricao=descricao, foto=foto, idCustomer=request.user.idCustomer, idOrder= idOrder)
            arte.save()
            messages.success(request, 'Muito Obrigado! Te avisaremos se precisarmos de mais alguma coisa')
            return redirect('arte_enviada')
    form = ArteForms(request.POST, request.FILES)
    return render(request, 'artCustomization/envio_de_arte.html', {"pedido": pedido, "form": form} )

def arte_enviada(request):
    return render(request, 'artCustomization/teste_aviso.html')