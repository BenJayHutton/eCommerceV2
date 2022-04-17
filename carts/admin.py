from django.contrib import admin
from .models import Cart, CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    search_fields = ['product__title', 'price_of_item', 'session_id']
    list_display = ['product', 'price_of_item', 'quantity', 'total']
    
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    search_fields = ['user__email', 'user__full_name', 'cart_items__session_id']
    list_display = ['user','subtotal', 'no_of_items_in_cart']
