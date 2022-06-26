from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Customer(AbstractUser):
    phone = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=15, null=True)
    displayName = models.CharField(max_length=255, null=True)
    photoUrl = models.TextField(max_length=1023, null=True)