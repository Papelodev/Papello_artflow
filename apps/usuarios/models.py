from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    # Add your additional fields here

    def __str__(self):
        return self.username if self.username else ''
