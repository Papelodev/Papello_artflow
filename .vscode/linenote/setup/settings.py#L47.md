from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

def upload_file_path(instance, filename, field_name):
    folder_path = f"arts/{instance.customer.id}/{instance.order.id}/{field_name}"
    return folder_path + '/' + filename

class Arte(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    # Additional fields for Arte
    instructions = models.CharField(max_length=500)
    reference_files = models.FileField(upload_to=partial(upload_file_path, field_name='references'), blank=True)
    mockup = models.ImageField(upload_to=partial(upload_file_path, field_name='mockup'), blank=True)
    alteracoes = models.CharField(max_length=500)
    altera_files = models.ImageField(upload_to=partial(upload_file_path, field_name='alterafiles'), blank=True)
    alteracounter = models.PositiveIntegerField(default=0)
    artefinal = models.ImageField(upload_to=partial(upload_file_path, field_name='artefinal'), blank=True)
    # ...
