from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40, default=None)
    nmID = models.IntegerField(default=None, primary_key=True)
    imtID = models.IntegerField(default=None)
    vendorCode = models.CharField(max_length=40, default=None)
    quantity = models.IntegerField(default=0, null=True)
    price = models.CharField(max_length=60, default=None, null=True)
    sizes = models.CharField(max_length=60, default=None, null=True)
    brand = models.CharField(max_length=75, default=None)
    category = models.CharField(max_length=100, default=None)
    photo = models.CharField(default=None, max_length = 255, null=True)
    

    def __str__(self):
        return f"{self.name}"

class Goods(models.Model):
    vendorCode = models.CharField(max_length=75)
    sku = models.CharField(max_length=30, default=None, primary_key=True)
    imtID = models.IntegerField(default=None)
    size = models.CharField(max_length=50)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, null=True)
    inWayToClient = models.IntegerField(default=0, null=True)
    inWayFromClient = models.IntegerField(default=0, null=True)
    quantityFull = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(default=0, null=True)
    editableSizePrice = models.BooleanField(default=False, null=True)
    discountedPrice = models.FloatField(default=None, null=True)
    discount = models.IntegerField(default=None, null=True)
    price = models.IntegerField(default=None, null=True)
    photo = models.CharField(default=None, max_length = 255, null=True)

class WarehouseData(models.Model):
    warehouseName = models.CharField(default=None, max_length=100)
    sku = models.ForeignKey(Goods, on_delete=models.CASCADE, default=None)
    constraint = models.UniqueConstraint(fields=['warehouseName', 'sku'], name='unique_field')
    lastChangeDate = models.DateTimeField(default=None)
    inWayToClient = models.IntegerField(default=None)
    inWayFromClient = models.IntegerField(default=None)
    quantityFull = models.IntegerField(default=None)
    quantity = models.IntegerField(default=None)
