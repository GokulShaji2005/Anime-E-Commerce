from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer

class ProductListApiView(ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.filter(is_active=True)

    filter_backends=[
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    ]

filterset_fields=["category"]
search_fields=["name","description"]
ordering_fields=["price"]