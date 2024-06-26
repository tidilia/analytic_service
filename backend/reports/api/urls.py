from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import salesViewSet, returnsViewSet, storageViewSet, logisticsViewSet, othersViewSet

reports_router = DefaultRouter()
viewsArray = [salesViewSet, returnsViewSet, storageViewSet, logisticsViewSet, othersViewSet]
addressArray = ['sales', 'returns', 'storage', 'logistics', 'other']
for i in range(len(addressArray)):
    url = 'reports/' + addressArray[i]
    reports_router.register(url, viewsArray[i])