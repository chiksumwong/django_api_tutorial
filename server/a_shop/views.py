from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from a_shop.permissions import IsPublicList
from a_shop.serializers import *


class MayorViewSet(viewsets.ModelViewSet):
    queryset = Mayor.objects.all()
    serializer_class = MayorSerializer
    permission_classes = [IsAdminUser]


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAdminUser]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsPublicList]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

