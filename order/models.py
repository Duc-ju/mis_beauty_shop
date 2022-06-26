from django.db import models
from customer.models import Customer
from service.models import ServiceOptions
# Create your models here.

class Cart(models.Model):
    status = models.CharField(max_length=255, default=None)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    canceledAt = models.DateTimeField(auto_now=True)
    customer = models.ManyToManyField(Customer, related_name='carts')
    serviceOption = models.ForeignKey(ServiceOptions, on_delete=models.CASCADE, related_name='cart')

class Billing(models.Model):
    serviceFee = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    income = models.FloatField(default=0)
    refund = models.FloatField(default=0)
    paymentMethod = models.CharField(max_length=255, default=None)
    star = models.IntegerField(default=5)
    feedback = models.TextField(max_length=4095, default=None)
    note = models.TextField(max_length=4095, default=None)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    canceledAt = models.DateTimeField(auto_now=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='billing')
