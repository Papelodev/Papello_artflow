from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth. models import User

class Fotografia(models.Model):

    OPCOES_CATEGORIA =[
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank = False)
    legenda = models.CharField(max_length=150, null=False, blank = False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default='')
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
    
class Artes(models.Model):

    descricao =  models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to= "artes/", blank=True)
    idCustomer = models.CharField(null=True, max_length=20)
    idOrder = models.CharField(null=True,  max_length=20)

    def __str__(self):
        return  self.descricao

    def set_customer(self, customer):
        self.idCustomer.set([customer])