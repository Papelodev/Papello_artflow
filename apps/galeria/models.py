from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from functools import partial
from apps.customers.models import CustomerProfile
from apps.orders.models import Order



def upload_file_path(instance, filename, field_name):
        # Construct the folder path based on the field name, idCustomer, and idOrder fields
        folder_path = f"arts/{instance.idCustomer}/{instance.idOrder}/{field_name}"
        return folder_path + '/' + filename

class Arte(models.Model):


    STATUS = [
    ( "Envio de arte", (
        ("AGUARDANDO", "Aguardando"),
        ("ENVIADO", "Enviado"),
        ("APROVADO", "Aprovado"),
    )),
    ("Confecção", (
        ("AGUARDANDO", "Aguardando"),
        ("EM_ANDAMENTO", "Em andamento"),
        ("CONCLUÍDO", "Concluído"),
    )),
    ( "Aprovação", (
        ("AGUARDANDO", "Aguardando"),
        ("ALTERAÇÃO", "Alteração"),
        ("APROVADA", "Aprovada"),
    )),
    ]

    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default='ENVIO-AGUARDANDO')
    idCustomer = models.IntegerField(null=False, blank = False)
    idOrder = models.IntegerField(null=False, blank = False)



    #referências para confecção
    instructions = models.CharField(max_length=500, null=False, blank = False)
    referencefiles = models.FileField(upload_to=partial(upload_file_path, field_name='references'), blank=True)

    #arquivo para aprovação
    mockup = models.ImageField(upload_to=partial(upload_file_path, field_name='mockup'), blank=True)

    #Alteração   
    alteracoes = models.CharField(max_length=500, null=False, blank = False)  #instruções de alteração    
    alterafiles = models.ImageField(upload_to=partial(upload_file_path, field_name='alterafiles'), blank=True) #armazena arquivos para alterações    
    alteracounter = alteracounter = models.PositiveIntegerField(default=0) #conta numero de alterações

    #arquivo final de arte aprovada
    artefinal = models.ImageField(upload_to=partial(upload_file_path, field_name='artefinal'), blank=True)

    
class Fotografia(models.Model):

  

    STATUS =[
        ("BRIEFING","Briefing"),
        ("REVISÃO","Revisão"),
        ("CONFECÇÃO","Confecção"),
        ("ALTERAÇÃO","Alteração"),
        ("APROVAÇÃO","Aprovação"),
        ("APROVADA","Aprovada"),
    ]

    nome = models.CharField(max_length=100, null=False, blank = False)
    legenda = models.CharField(max_length=150, null=False, blank = False)
    categoria = models.CharField(max_length=100,choices=STATUS, default='')
    descricao = models.TextField(null=False, blank = False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self):
        return  self.nome