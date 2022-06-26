from django.db import models

# Create your models here.
class ColorOption(models.Model):
    name = models.TextField(max_length=1023, default=None)
    colorCode = models.CharField(max_length=15, default=None)

class TypeOption(models.Model):
    name = models.TextField(max_length=1023, default=None)
    imageLink = models.TextField(max_length=1023, default=None)

class Service(models.Model):
    name = models.TextField(max_length=1023, default=None)
    description = models.TextField(max_length=8191, default=None)

class ServiceImage(models.Model):
    link = models.TextField(max_length=4095, default=None)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')

class ServiceOptions(models.Model):
    price = models.FloatField(default=0)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='option')
    color = models.ForeignKey(ColorOption, on_delete=models.CASCADE, related_name='color')
    type = models.ForeignKey(TypeOption, on_delete=models.CASCADE, related_name='type')
