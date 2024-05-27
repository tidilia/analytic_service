from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import createSeo

# seo_product_router = DefaultRouter()
# seo_product_router.register(r'seo', createSeo)
urlpatterns = [
    path('create/', createSeo.as_view())
]