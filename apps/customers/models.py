from django.db import models
from apps.usuarios.models import MyUser
from datetime import datetime

class CustomerProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    email = models.EmailField()
    idCustomer = models.IntegerField()
    nameCustomer = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    birthDate = models.DateField()
    typeCustomer = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    billingAddress = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    cpf_cnpj = models.CharField(max_length=20)
    rg_ie = models.CharField(max_length=20)
    customerExternalId = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nameCustomer
