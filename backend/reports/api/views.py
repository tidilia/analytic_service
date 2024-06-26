from rest_framework.status import HTTP_201_CREATED
from rest_framework import response
from rest_framework.viewsets import ModelViewSet
from . import dataHandler
from ..models import sales, returns, logistics, other, storage
from .serializers import salesSerializer, storageSerializer, logisticsSerializer, returnsSerializer, otherSerializer
    
class salesViewSet(ModelViewSet):
    dataHandler.update_database()
    queryset = sales.objects.all()
    serializer_class = salesSerializer

class storageViewSet(ModelViewSet):
    dataHandler.update_database()
    queryset = storage.objects.all()
    serializer_class = storageSerializer

class logisticsViewSet(ModelViewSet):
    dataHandler.update_database()
    queryset = logistics.objects.all()
    serializer_class = logisticsSerializer

class returnsViewSet(ModelViewSet):
    dataHandler.update_database()
    queryset = returns.objects.all()
    serializer_class = returnsSerializer

class othersViewSet(ModelViewSet):
    dataHandler.update_database()
    queryset = other.objects.all()
    serializer_class = otherSerializer
