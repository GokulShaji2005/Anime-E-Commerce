from rest_framework import serializers
from .models import Product,ProductVariant


class ProductVariantSerializer(serializers.ModelSerializer):
     class Meta:
          model:ProductVariant
          fields = [
            "id",
            "variant_name"
            "price",
            "stock",
        
        ]

class ProductSerializer(serializers.ModelSerializer):
    variant = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "price",
            "image",
            "stock",
            "is_active",
            "variant",
        ]
