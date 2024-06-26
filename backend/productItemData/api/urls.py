from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import getDayOrders, getWeekOrders, getConversions, getRealPrice

# seo_product_router = DefaultRouter()
# seo_product_router.register(r'seo', createSeo)
urlpatterns = [
    path('getDayOrders/', getDayOrders.as_view()),
    path('getWeekOrders/', getWeekOrders.as_view()),
    path('getConversions/', getConversions.as_view()),
    path('getRealPrice/', getRealPrice.as_view())
]