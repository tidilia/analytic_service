from django.db import models
from products.models import Product
# Create your models here.


class productDayOrders(models.Model):
    date = models.DateTimeField(default=None)
    time = models.IntegerField(default=None)
    nmID = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, null=True)
    sku = models.CharField(max_length=30, default=None)
    size = models.CharField(max_length=30, default=None)


class productWeekOrders(models.Model):
    date = models.DateField(default=None)
    time = models.IntegerField(default=None)
    nmID = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, null=True)
    sku = models.CharField(max_length=30, default=None)
    size = models.CharField(max_length=30, default=None)
