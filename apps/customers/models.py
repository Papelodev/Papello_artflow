from django.db import models
from apps.usuarios.models import MyUser
from datetime import datetime

class CustomerProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    # Additional fields for customer profile
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=datetime.now, blank=False)
    # ...

class Order(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    order_number = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Additional fields for order
    order_date = models.DateField()
    status = models.CharField(max_length=50)
    
    # ...

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Additional fields for payment
    payment_date = models.DateField()
    # ...
