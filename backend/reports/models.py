from django.db import models
from products.models import Product

class storage(models.Model):
    storaging = models.FloatField(default=0)
    recount_storaging = models.FloatField(default=0)
    acceptanse = models.FloatField(default=0)

class sales(models.Model):
    real_price = models.FloatField(default=0)
    comission = models.FloatField(default=0)
    income = models.FloatField(default=0)
    product_name = models.CharField(max_length=50)
    nm_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, null=True)

class returns(models.Model):
    nm_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, null=True)
    product_name = models.CharField(max_length=50)
    refund_amount = models.FloatField(default=0)

class logistics(models.Model):
    number = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    average_price = models.FloatField(default=0)

class other(models.Model):
    fines = models.FloatField(default=0)
    surchages = models.FloatField(default=0)
    compensation = models.FloatField(default=0)

class information(models.Model):
    date_from = models.DateTimeField(default=None)
    date_to = models.DateTimeField(default=None)
# Create your models here.
