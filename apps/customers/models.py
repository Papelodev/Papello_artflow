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
    customerExternalId = models.CharField(max_length=255)

    def __str__(self):
        return self.nameCustomer

class Order(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    order_number = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Additional fields for order
    order_date = models.DateField()
    status = models.CharField(max_length=50)
    
   

