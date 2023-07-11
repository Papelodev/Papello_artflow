from django import template

from apps.galeria.models import Arte

register = template.Library()

#Função utilizada para iterar sobre os produtos de um kit no template 'customizacao'
@register.filter
def get_item(lst, index):
    return lst[index - 1]["name"]


#Função que retorna o status de cada produto do pedido para o template 'detalhe_pedido'
@register.filter
def get_art(idProduct, idOrder):

    if Arte.objects.filter(idProduct=idProduct, idOrder=idOrder).exists():
        art_count = Arte.objects.filter(idProduct=idProduct, idOrder=idOrder).count()
        print(art_count)

        if art_count == 1:  
        # Apenas um objeto encontrado
            art = Arte.objects.get(idProduct=idProduct, idOrder=idOrder)
            return {'status': art.status, 'id': art.id}
        if art_count > 1:
            # Mais de um objeto encontrado
            # Faça algo aqui
            art = Arte.objects.filter(idProduct=idProduct, idOrder=idOrder)
            return art
    else:
        return {'status':'Aguardando Envio'}

#Função para calcular o valor total de cada produto baseado na quantidade   
@register.filter
def mul(quantity, value):
    return quantity * value