from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, getProductById

product_router = DefaultRouter()
product_router.register(r'products', ProductViewSet)

urlpatterns = [
    path('getProduct/', getProductById.as_view())
]