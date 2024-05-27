from rest_framework.viewsets import ModelViewSet
from ..models import Product
from .serializers import ProductSerializer
from ..dataParser import goods_importer, price_importer, quantity_importer

class ProductViewSet(ModelViewSet):
    goods_importer.update_database()
    price_importer.update_database()
    quantity_importer.update_database()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
