from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from app.products.models import Product, ProductVariant  # assuming Product and ProductVariant are in products app

# Cart model: one cart per user (optional if you want guest carts, we can adjust)
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    @property
    def total_price(self):
        total = sum(item.total_price for item in self.items.all())
        return total


# Items inside the cart
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, null=True, blank=True, on_delete=models.SET_NULL)  # optional if no variants
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("cart", "product", "variant")  # prevent duplicate entries for same variant

    def __str__(self):
        if self.variant:
            return f"{self.product.name} ({self.variant.variant_name}) x {self.quantity}"
        return f"{self.product.name} x {self.quantity}"

    @property
    def total_price(self):
        price = self.variant.price if self.variant and self.variant.price else self.product.price
        return price * self.quantity
