from django.db import models
from products.models import Product

class CartItem(models.Model):
    product     = models.ForeignKey(Product, default=None, blank=True, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=0, null=True)


class Cart(models.Model):
    cartItem    = models.ManyToManyField(CartItem, default=None, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)