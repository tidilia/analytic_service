from rest_framework import serializers
from ..models import sales, returns, storage, logistics, other


class salesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sales
        fields = '__all__'

class returnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = returns
        fields = '__all__'

class storageSerializer(serializers.ModelSerializer):
    class Meta:
        model = storage
        fields = '__all__'

class logisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = logistics
        fields = '__all__'

class otherSerializer(serializers.ModelSerializer):
    class Meta:
        model = other
        fields = 'fines', 'surchages', 'compensation'