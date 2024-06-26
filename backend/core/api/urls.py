from rest_framework.routers import DefaultRouter
from products.api.urls import product_router
from django.urls import path, include
from seo.api import urls as seo_urls
from productItemData.api import urls as product_item_urls
from products.api import urls as products_urls
from reports.api.urls import reports_router

router = DefaultRouter()

# products
router.registry.extend(product_router.registry)
#reports
router.registry.extend(reports_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('seo/', include(seo_urls)),
    path('productItemData/', include(product_item_urls)),
    path('',include(products_urls) )
]
