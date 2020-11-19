from django.urls import path, include

from .views import (CustomerViewSet,
                    ProductViewSet,
                    OrderViewSet,
                    OrderItemViewSet,
                    ShippingAddressViewSet)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('order', OrderViewSet, basename='order')
router.register('orderitem', OrderItemViewSet, basename='orderitem')
router.register('shippingaddress', ShippingAddressViewSet, basename='shippingaddress')
router.register('customer', CustomerViewSet, basename='customer')



urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
