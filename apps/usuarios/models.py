from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # Custom user fields
    # Add your additional fields here

    def __str__(self):
        return self.user.username if self.user else ''
