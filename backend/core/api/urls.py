from rest_framework.routers import DefaultRouter
from products.api.urls import product_router
from django.urls import path, include
from seo.api import urls

router = DefaultRouter()

# products
router.registry.extend(product_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('seo/', include(urls))
]
