from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class MyUser(AbstractUser):
    # Add your additional fields here
    idCustomer = models.IntegerField(null=True)
    cpf_cnpj = models.CharField(max_length=20)

    groups = models.ManyToManyField(Group, related_name='myusers')
    user_permissions = models.ManyToManyField(Permission, related_name='myusers')

    def __str__(self):
        return self.username if self.username else ''
