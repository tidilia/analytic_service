from rest_framework import serializers
from ..models import productDayOrders

class dayOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = productDayOrders
        fields = 'date', 'time', 'nmID', 'sku', 'size'

class weekOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = productDayOrders
        fields = 'date', 'time', 'nmID', 'sku', 'size'
