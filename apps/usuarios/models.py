from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'customer'),
      (2, 'admin'),
      (3, 'designer'),
      (4, 'reviewer'),
      (5, 'employee'),
  )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)

    def __str__(self):
        return self.username if self.username else ''
