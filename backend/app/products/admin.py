from django.contrib import admin

from django.contrib import admin
from .models import Product, ProductVariant, Category
from django.contrib import admin
from .models import Product, ProductVariant, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","description","price", "stock", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name",)

admin.site.register(ProductVariant)
admin.site.register(Category)
