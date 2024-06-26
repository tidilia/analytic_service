from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from ..models import Product
from .serializers import ProductsSetSerializer, ProductSerializer
from ..dataParser import goods_importer, price_importer, quantity_importer
from rest_framework.status import HTTP_201_CREATED
from rest_framework import response

class ProductViewSet(ModelViewSet):
    goods_importer.update_database()
    price_importer.update_database()
    quantity_importer.update_database()
    queryset = Product.objects.all()
    serializer_class = ProductsSetSerializer


class getProductById(APIView):
    def post(self, request, format=None):
        product_id = request.data.get("nmID")
        data = Product.objects.filter(nmID=product_id)
        #print(Product.objects.all())
        print(Product.objects.filter(nmID=product_id))
        serializer = ProductSerializer(data, many=True)
        return response.Response(serializer.data, content_type='application/json', status=HTTP_201_CREATED)

