from django.shortcuts import render, redirect, get_object_or_404

from apps.orders.models import Order, OrderProduct, Product

from apps.galeria.models import Arte

from apps.usuarios.models import MyUser

from apps.customers.models import CustomerProfile

from apps.galeria.forms import ArteForms, PrototipoForms, AlteracaoForms

from apps.orders.forms import Art_quantity_forms

import requests

from django.contrib import auth, messages

from django.http import HttpResponseRedirect

from django.urls import reverse
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
    produtos_pedido = list(OrderProduct.objects.filter(order=pedido))

    #Verifica se o pedido já tem uma arte enviada (LEMBRAR DE MUDAR O FILTER PARA GET DEPOIS)
    arts = Arte.objects.filter(idOrder=idOrder)
    art = arts.first()
    if arts.exists():
        return render(request, 'orders/detalhe_pedido.html', {'pedido': pedido, 'produtos': produtos_pedido, 'art': art})  
    produtos_associados = list(Product.objects.filter(orderproduct__in=produtos_pedido))
    produtos_combinados = zip(produtos_associados, produtos_pedido)
    for produto, produtos_pedido in produtos_combinados:
       produto.quantity = produtos_pedido.quantity

    print(pedido)
    return render(request, 'orders/detalhe_pedido.html', {'pedido': pedido, 'produtos': produtos_associados, 'art': art})

def customizacao(request, idOrder, indice):
    pedido = get_object_or_404(Order, idOrder=idOrder)
    produtos_pedido = list(OrderProduct.objects.filter(order=pedido))
    produtos_associados = list(Product.objects.filter(orderproduct__in=produtos_pedido,  isCustomizeable=True))
    produtos_kit = list(Product.objects.filter(is_kit=True,  isCustomizeable=True))
    produtos_combinados = zip(produtos_associados, produtos_pedido)
    for produto, produtos_pedido in produtos_combinados:
       produto.quantity = produtos_pedido.quantity

    produtos_associados = [produto for produto in produtos_associados if not produto.is_kit]

    for produto_kit in produtos_kit:
        for produto in produto_kit.products_kit:
            produtos_associados.append(produto)

    produto_atual = produtos_associados[indice]
    form = Art_quantity_forms(quantidade_produtos=produto_atual.quantity)
    if request.method =='POST':
        #if form.is_valid():
            print('Entrous')
            quantidade_artes = int(request.POST.get('quantidade_artes'))
            quantidade_produtos = produto_atual.quantity

            # Calcular a quantidade de produtos disponíveis para cada arte
            quantidade_por_arte = quantidade_produtos // quantidade_artes
            
            # Gerar as opções de arte com base na quantidade disponível
            opcoes_artes = []
            for i in range(quantidade_artes):
                opcoes_artes.append({
                    'arte_numero': i + 1,
                    'quantidade_produtos': quantidade_por_arte
                })
            # Passar as opções de arte para o template
            return render(request, 'orders/customizacao.html', {'pedido': pedido, 'produto': produto_atual, 'form': form, 'opcoes_arte': opcoes_artes})



    return render(request, 'orders/customizacao.html', {'pedido': pedido, 'produto': produto_atual, 'form': form})

def envio_de_arte(request, idOrder, indice):
    pedido = get_object_or_404(Order, idOrder=idOrder)
    produtos_pedido = list(OrderProduct.objects.filter(order=pedido))
    indice_produto = int(indice) if indice else 0
    print(indice_produto)
        
    produtos_associados = list(Product.objects.filter(orderproduct__in=produtos_pedido,  isCustomizeable=True))
    produtos_kit = list(Product.objects.filter(is_kit=True,  isCustomizeable=True))
    produtos_combinados = zip(produtos_associados, produtos_pedido)
    for produto, produtos_pedido in produtos_combinados:
       produto.quantity = produtos_pedido.quantity

    produtos_associados = [produto for produto in produtos_associados if not produto.is_kit]

    for produto_kit in produtos_kit:
        for produto in produto_kit.products_kit:
            produtos_associados.append(produto)

    produto_atual = produtos_associados[indice]
    print(produto_atual)
    if(produto_atual.quantity > 1):
        pedido = get_object_or_404(Order, idOrder=idOrder)
        return redirect(f'/customizacao/{idOrder}/{indice}')

    if request.method =='POST':
        form = ArteForms(request.POST, request.FILES)
        if form.is_valid():
            customer = CustomerProfile.objects.get(user=request.user)
            instructions = request.POST.get('instructions')
            referencefiles = request.FILES.get('referencefiles')
            idCustomer = customer.idCustomer
            statusEnviado = "ENVIADO"
            print(produto_atual)

            if isinstance(produto_atual, dict):

                if 'idProduct' in produto_atual:
                    idProduct = produto_atual['idProduct']
            else:
                idProduct = produto_atual.product_id
                orderProduct = OrderProduct.objects.get(product=produto_atual, order=pedido)
            arte = Arte(
                instructions=instructions,
                referencefiles=referencefiles,
                idCustomer=idCustomer,
                idOrder=idOrder,
                idProduct=idProduct,
                orderProduct=orderProduct,
                status=statusEnviado)
            arte.save()
            messages.success(request, 'Arquivos enviados!')
            return redirect(f'/envio-de-arte/{idOrder}/{indice + 1}')

    form = ArteForms(request.POST, request.FILES)

    return render(request, 'orders/envio_de_arte.html', {'pedido': pedido, 'produto': produto_atual, 'form': form, 'indice_produto': indice_produto})

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
    form = AlteracaoForms(request.POST, request.FILES)
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
            form = AlteracaoForms(request.POST, request.FILES)
            if form.is_valid():
                alterafiles = request.FILES.get('alterafiles')
                art.status="ALTERAÇÃO"
                art.alteracounter += 1
                art.alterafiles = alterafiles
                art.save()
                messages.error(request, 'Alteração Solicitada')
        return redirect('meus_pedidos')

