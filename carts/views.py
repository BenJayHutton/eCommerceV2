from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpRequest

from products.models import Product
from .models import Cart, CartItem

class CartHome(ListView):
    template_name = "carts/home.html"

    def get(self, request):
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context = {
            "cart_obj": cart_obj,
        }
        return render(request,"carts/home.html", context)

def cart_update(request, *args, **kwargs):
    product_id = request.POST.get('product_id', None)
    product_quantity = request.POST.get('product_quantity', None)
    cart_item_update = request.POST.get('cart_item_update', False)
    cart_item_remove = request.POST.get('cart_item_remove', False)
    product_obj = Product.objects.get(id=product_id)
    if product_obj is not None:
        cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_obj=product_obj, product_quantity=product_quantity)
        cart_obj, new_obj = Cart.objects.new_or_get(request)

        if cart_item_obj in cart_obj.cart_items.all() and cart_item_remove:
            cart_obj.cart_items.remove(cart_item_obj)        
        else:
            cart_obj.cart_items.add(cart_item_obj)

        if cart_item_obj in cart_obj.cart_items.all() and cart_item_update:
            cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_obj=product_obj, product_quantity=product_quantity)
        request.session['cart_items'] = cart_obj.cart_items.count()
    return redirect("cart:cart")