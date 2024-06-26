from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED
from rest_framework import response
from . import dataHandler
from ..models import productDayOrders, productWeekOrders
from .serializers import dayOrdersSerializer, weekOrdersSerializer
# class seoProductViewSet(ModelViewSet):
#     queryset = seoProduct.objects.all()
#     serializer_class = ProductSerializer


class getWeekOrders(APIView):
    def post(self, request, format=None):
        product_id = request.data.get("nmID")
        data = productWeekOrders.objects.filter(nmID=product_id)
        serializer = weekOrdersSerializer(data, many=True)
        return response.Response(serializer.data, content_type='application/json', status=HTTP_201_CREATED)
        # return response.Response(t, status=HTTP_201_CREATED)


class getDayOrders(APIView):
    def post(self, request, format=None):
        dataHandler.update_database()
        product_id = request.data.get("nmID")
        data = productDayOrders.objects.filter(nmID=product_id)
        serializer = dayOrdersSerializer(data, many=True)
        return response.Response(serializer.data, content_type='application/json', status=HTTP_201_CREATED)
    
class getConversions(APIView):
    def post(self, request, format=None):
        product_id = request.data.get("nmID")
        data = dataHandler.get_conversia(product_id)
        return response.Response(data, status=HTTP_201_CREATED)
    
class getRealPrice(APIView):
    def post(self, request, format=None):
        product_id = request.data.get("nmID")
        data = dataHandler.get_real_price(product_id)
        return response.Response(data, status=HTTP_201_CREATED)