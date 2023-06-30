from django.shortcuts import render, redirect, get_object_or_404

from apps.orders.models import Order, OrderProduct, Product

from apps.galeria.models import Arte

from apps.usuarios.models import MyUser

from apps.customers.models import CustomerProfile

from apps.galeria.forms import ArteForms, PrototipoForms

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
    
    if request.user.user_type == 3:
        arts = Arte.objects.all()
        print(arts)
        
        return render(request, 'designer/designer_home.html', {"arts": arts} )

    if request.user.user_type == 4:
        arts = Arte.objects.filter(status="ENVIADO")

        return render(request, 'reviewer/reviewer_home.html', {"arts": arts} )

def detalhe_pedido(request, idOrder):
    pedido = get_object_or_404(Order, idOrder=idOrder)
    produtos_pedido = OrderProduct.objects.filter(order=pedido)

    #Verifica se o pedido já tem uma arte enviada (LEMBRAR DE MUDAR O FILTER PARA GET DEPOIS)
    arts = Arte.objects.filter(idOrder=idOrder)
    art = arts.first()
    if arts.exists():
        return render(request, 'orders/detalhe_pedido.html', {'pedido': pedido, 'produtos': produtos_pedido, 'art': art})  
    #produtos_ids = [produto.id for produto in produtos_pedido]
    #produtos_associados = Product.objects.filter(id__in=produtos_ids)
    #print(produtos_associados)
    return render(request, 'orders/detalhe_pedido.html', {'pedido': pedido, 'produtos': produtos_pedido, 'art': art})

def customizacao(request, idOrder):
    pedido = get_object_or_404(Order, idOrder=idOrder)
    produtos_pedido = OrderProduct.objects.filter(order=pedido)
    return render(request, 'orders/customizacao.html', {'pedido': pedido, 'produtos': produtos_pedido})

def envio_de_arte(request, idOrder):
    pedido = get_object_or_404(Order, idOrder=idOrder)
    produtos_pedido = OrderProduct.objects.filter(order=pedido)
    if request.method =='POST':
        form = ArteForms(request.POST, request.FILES)
        if form.is_valid():
            customer = CustomerProfile.objects.get(user=request.user)

            #Busca os ids dos produtos que estão em OrderProducts

            produtos_ids = [produto.id for produto in produtos_pedido]
            
            #Seleciona os mesmos produtos que estão em OrderProducts, na tabela Products para pegar o idProduct de cada um.

            produtos_associados = Product.objects.filter(id__in=produtos_ids)

            instructions = request.POST.get('instructions')
            referencefiles = request.FILES.get('referencefiles')
            idCustomer = customer.idCustomer
            statusEnviado = "ENVIADO" 

            #Salva arte enviada pelo cliente na tabela Arte
            arte = Arte(
                instructions=instructions,
                referencefiles=referencefiles,
                idCustomer=idCustomer, idOrder=idOrder,
                idProduct=produtos_associados[0].product_id,
                status=statusEnviado)
            arte.save()
            messages.success(request, 'Muito Obrigado! Te avisaremos se precisarmos de mais alguma coisa')
            return redirect('detalhe_pedido', idOrder=idOrder)
    form = ArteForms(request.POST, request.FILES)
    return render(request, 'orders/envio_de_arte.html', {'pedido': pedido, 'produtos': produtos_pedido, 'form': form})

def arte_finalizada(request):
    return render(request, 'orders/arte_finalizada.html')

def aprova_arte(request, artId, isApproved):
    art = Arte.objects.get(id=artId)
    if(isApproved):
        art.status="APROVADO"
        art.save()
        messages.success(request, 'Arte Aprovada')
    else:
        art.status="AGUARDANDO"
        art.save()
        messages.error(request, 'Arte Reprovada')
    return redirect('meus_pedidos')
    

def detalhe_arte(request, artId):
    art = Arte.objects.get(id=artId)
    customer= CustomerProfile.objects.get(idCustomer=art.idCustomer)
    order= Order.objects.get(idOrder=art.idOrder)
    product = Product.objects.get(product_id=art.idProduct)
    form = PrototipoForms(request.POST, request.FILES)
    context = {
        'artStatus': art.status,
        'artId': artId,
        'idOrder': art.idOrder,
        'nameClient':customer.nameCustomer,
        'productName': product.product_name,
        'referenceFiles': art.referencefiles,
        'instructions': art.instructions,
        'date': art.date,
        'form': form
    }

    #Verifica status da arte e se tiver APROVADO ou EM ENDAMENTO é redirecionada para tela arte_aprovada DO Designer
    if art.status in ["APROVADO", "EM_ANDAMENTO", "CONCLUÍDO", "ALTERAÇÃO"]:
        
        return render(request, 'designer/detalhe_arte_aprovada.html', context)

    return render(request, 'reviewer/detalhe_arte.html', context)

def envio_prototipo(request, artId):
    form = PrototipoForms(request.POST, request.FILES)
    if request.method =='POST':
        if form.is_valid():
            art = Arte.objects.get(id=artId)
            mockup = request.FILES.get('mockup')

            #Salva mockup enviado pelo designer na tabela Arte
            art.mockup = mockup
            art.status="CONCLUÍDO"
            art.save()
            messages.success(request, 'Protótipo Enviada')
            arts = Arte.objects.all()
            return render(request, 'designer/designer_home.html', {'arts': arts})
    
def pegar_card(request, artId):
    art = Arte.objects.get(id=artId)
    art.status="EM_ANDAMENTO"
    art.save()
    arts = Arte.objects.all()
    return render(request, 'designer/designer_home.html', {'arts': arts})

def verifica_prototipo(request, idOrder):
    art = Arte.objects.get(idOrder=idOrder)
    customer= CustomerProfile.objects.get(idCustomer=art.idCustomer)
    order= Order.objects.get(idOrder=art.idOrder)
    product = Product.objects.get(product_id=art.idProduct)
    form = PrototipoForms(request.POST, request.FILES)
    context = {
        'artStatus': art.status,
        'artId': art.id,
        'idOrder': art.idOrder,
        'nameClient':customer.nameCustomer,
        'productName': product.product_name,
        'mockup': art.mockup,
        'instructions': art.instructions,
        'date': art.date,
        'form': form
    }
    return render(request, 'orders/verifica_prototipo.html', context)

def aprova_prototipo(request, artId, isApproved):
        art = Arte.objects.get(id=artId)
        if(isApproved):
            art.status="APROVADA"
            art.save()
            messages.success(request, 'Protótipo Aprovado')
        else:
            art.status="ALTERAÇÃO"
            art.alteracounter += 1
            art.save()
            messages.error(request, 'Alteração Solicitada')
        return redirect('meus_pedidos')