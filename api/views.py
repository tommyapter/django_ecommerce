from store.models import (Customer,
                        Product,
                        Order,
                        OrderItem,
                        ShippingAddress,
                        )

from .serializers import (CustomerSerializer,
                        ProductSerializer,
                        OrderSerializer,
                        OrderItemSerializer,
                        ShippingAddressSerializer,
                        )

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
                                        # , IsAccountAdminOrReadOnly
from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class ShippingAddressViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingAddressSerializer
    queryset = ShippingAddress.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
