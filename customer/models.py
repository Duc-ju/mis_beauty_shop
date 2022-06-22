from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Customer(AbstractUser):
    phone = models.CharField(max_length=15, default=None)
    gender = models.CharField(max_length=15, default=None)
    displayName = models.CharField(max_length=255)
    photoUrl = models.TextField(max_length=1023)