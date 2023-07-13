from django.shortcuts import render, redirect, get_object_or_404

from apps.orders.models import Order, OrderProduct, Product

from apps.galeria.models import Arte

from apps.usuarios.models import MyUser

from apps.customers.models import CustomerProfile

from apps.galeria.forms import ArteForms, PrototipoForms, AlteracaoForms, rejectionReviewerForm

from apps.orders.forms import Art_quantity_forms

from collections import namedtuple

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
    produtos_associados = list(Product.objects.filter(orderproduct__in=produtos_pedido))
    produtos_combinados = zip(produtos_associados, produtos_pedido)
    for produto, produtos_pedido in produtos_combinados:
       produto.quantity = produtos_pedido.quantity

    #Verifica se o pedido já tem uma arte enviada (LEMBRAR DE MUDAR O FILTER PARA GET DEPOIS)
    arts = Arte.objects.filter(idOrder=idOrder)
    if arts.exists():
        return render(request, 'orders/detalhe_pedido.html', {'pedido': pedido, 'produtos': produtos_associados, 'arts': arts})  
    print(pedido)
    return render(request, 'orders/detalhe_pedido.html', {'pedido': pedido, 'produtos': produtos_associados, 'arts': arts})

def customizacao(request, idOrder, indice):
    pedido = get_object_or_404(Order, idOrder=idOrder)
    produtos_pedido = list(OrderProduct.objects.filter(order=pedido))
    produtos_associados = list(Product.objects.filter(orderproduct__in=produtos_pedido,  isCustomizeable=True))
    produtos_kit = list(Product.objects.filter(is_kit=True,  isCustomizeable=True))
    produtos_combinados = zip(produtos_associados, produtos_pedido)
    for produto, produtos_pedido in produtos_combinados:
       produto.quantity = produtos_pedido.quantity

    produto_atual = None
    if indice < len(produtos_associados):
        produto_atual = produtos_associados[indice]
    if produto_atual.is_kit:
        form = Art_quantity_forms(quantidade_produtos=len(produto_atual.products_kit))
    else:
        form = Art_quantity_forms(quantidade_produtos=produto_atual.quantity)
    if request.method =='POST':
        #if form.is_valid():
        print('Entrou')
        quantidade_artes = int(request.POST.get('quantidade_artes'))
        quantidade_produtos = produto_atual.quantity

        # Calcular a quantidade de produtos disponíveis para cada arte
        quantidade_por_arte = quantidade_produtos // quantidade_artes 
            
        # Gerar as opções de arte com base na quantidade disponível
        opcoes_artes = []
        if produto_atual.is_kit:
            if isinstance(produto_atual.products_kit, dict):
                Objeto = namedtuple('Objeto', produto_atual.products_kit.keys())
                produto_atual.products_kit = Objeto(**produto_atual.products_kit)
        for i in range(quantidade_artes):
            opcoes_artes.append({
                'arte_numero': i + 1,
                'quantidade_produtos': quantidade_produtos
            })
        # Passar as opções de arte para o template
        return render(request, 'orders/customizacao.html', {'pedido': pedido, 'produto': produto_atual, 'form': form, 'opcoes_arte': opcoes_artes, 'indice': indice})



    return render(request, 'orders/customizacao.html', {'pedido': pedido, 'produto': produto_atual, 'form': form, 'indice': indice})


#Função utilizada para iterar o envio de artes quando o produto tiver a quantidade > 1.
def envio_de_arte_por_quantidade(request, idOrder, indice, artesQuantidade):
    pedido = get_object_or_404(Order, idOrder=idOrder)
    produtos_pedido = list(OrderProduct.objects.filter(order=pedido))
    indice_produto = int(indice)
    artesQuantidade = artesQuantidade - 1 
        
    produtos_associados = list(Product.objects.filter(orderproduct__in=produtos_pedido,  isCustomizeable=True))
    produtos_kit = list(Product.objects.filter(is_kit=True,  isCustomizeable=True))
    produtos_combinados = zip(produtos_associados, produtos_pedido)
    for produto, produtos_pedido in produtos_combinados:
       produto.quantity = produtos_pedido.quantity

    produto_atual = None
    if indice < len(produtos_associados):
        produto_atual = produtos_associados[indice]

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
            
            
            if produto_atual.is_kit:
                kit_counter = 0
                for product in produto_atual.products_kit:
                     if not Arte.objects.filter(idProduct=product['idProduct'], idOrder=idOrder).exists():
                        idProduct = produto_atual.products_kit[kit_counter]['idProduct']
                     else:
                        kit_counter += 1

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

    if(artesQuantidade < 0):
        return redirect(f'/envio-de-arte/{idOrder}/{indice + 1}')

    form = ArteForms(request.POST, request.FILES)

    return render(request, 'orders/envio_de_arte_por_quantidade.html', {'pedido': pedido, 'produto': produto_atual, 'form': form, 'indice_produto': indice_produto, 'artesQuantidade': artesQuantidade})



def envio_de_arte(request, idOrder, indice):
    pedido = get_object_or_404(Order, idOrder=idOrder)
    produtos_pedido = list(OrderProduct.objects.filter(order=pedido))
    indice_produto = int(indice) if indice else 0
        
    produtos_associados = list(Product.objects.filter(orderproduct__in=produtos_pedido,  isCustomizeable=True))
    produtos_combinados = zip(produtos_associados, produtos_pedido)
    for produto, produtos_pedido in produtos_combinados:
       produto.quantity = produtos_pedido.quantity

    produto_atual = None
    if indice < len(produtos_associados):
        produto_atual = produtos_associados[indice]

        #Verifica se o produto atual já possui uma arte, se possuir passa para o próximo
        if Arte.objects.filter(idProduct=produto_atual.product_id).exists():
            return redirect(f'/envio-de-arte/{idOrder}/{indice + 1}')

        if isinstance(produto_atual, dict):
            Objeto = namedtuple('Objeto', produto_atual.keys())
            produto_atual = Objeto(**produto_atual)

        print((produto_atual))
        if(produto_atual.quantity > 1 or produto_atual.is_kit):
            pedido = get_object_or_404(Order, idOrder=idOrder)
            return redirect(f'/customizacao/{idOrder}/{indice_produto}')

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
                    idProduct = produto_atual.product_id if hasattr(produto_atual, 'product_id') else produto_atual.idProduct

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
    if produto_atual == None:
        messages.success(request, 'Muito Obrigado! Te avisaremos se precisarmos de mais alguma coisa')
        return redirect('/meus-pedidos')

    form = ArteForms(request.POST, request.FILES)

    return render(request, 'orders/envio_de_arte.html', {'pedido': pedido, 'produto': produto_atual, 'form': form, 'indice_produto': indice_produto})

def arte_finalizada(request):
    return render(request, 'orders/arte_finalizada.html')

def aprova_arte(request, artId, isApproved):
    art = Arte.objects.get(id=artId)
    if(isApproved):
        art.status="APROVADO"
        art.save()
        messages.success(request, 'Arquivos Aprovados')
    if request.method == 'POST':
        form = rejectionReviewerForm(request.POST, request.FILES)
        rejection_reason = request.POST.get('rejection_reason')
        art.status="AGUARDANDO"
        art.rejection_reason = rejection_reason
        art.save()
        messages.error(request, 'Arquivos reprovados')
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

    form = rejectionReviewerForm()
    context['form'] = form
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
    art.status = "EM_ANDAMENTO"
    art.designer_responsible = request.user
    art.save()
    arts = Arte.objects.all()
    return render(request, 'designer/designer_home.html', {'arts': arts})

def verifica_prototipo(request, idOrder, idProduct, artId):
    art = Arte.objects.get(idOrder=idOrder, idProduct=idProduct, id=artId)
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

def arquivos_reprovados(request, artId):
    art = Arte.objects.get(id=artId)
    form = ArteForms(request.POST, request.FILES)
    if request.method =='POST':
        if form.is_valid():
            instructions = request.POST.get('instructions')
            referencefiles = request.FILES.get('referencefiles')
            print(referencefiles)
        
            art.instructions = instructions
            art.referencefiles = referencefiles
            art.status = "ENVIADO"
            art.save()
            messages.success(request, "Arquivos enviados")
            return redirect('meus_pedidos')
    return render(request, 'orders/arquivos_reprovados.html', {'art': art, 'form': form})