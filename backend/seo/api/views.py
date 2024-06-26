from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED
from rest_framework import response
from . import dataHandler
# class seoProductViewSet(ModelViewSet):
#     queryset = seoProduct.objects.all()
#     serializer_class = ProductSerializer

class createSeo(APIView):
    def post(self, request, format=None):
        id = request.data.get("nmID")
        features = request.data.get("description")
        t = dataHandler.makeDescription(id, features)
        return response.Response(t, status=HTTP_201_CREATED)
