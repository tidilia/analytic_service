from rest_framework import serializers
from ..models import Product

class ProductsSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'nmID', 'name', 'sizes', 'photo'