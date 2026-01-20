from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    # Stock represents total stock, variants can have specific stock
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 

class ProductVariant(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="variant")
    variant_name = models.CharField(max_length=100)  # e.g., "Small", "Large", "Red", "Blue"
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # override product price if needed
    stock = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.product.name} - {self.variant_name}"
