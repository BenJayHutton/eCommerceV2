from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpRequest

from orders.models import Order
from products.models import Product
from .models import Cart, CartItem

class CartHome(ListView):
    template_name = "carts/home.html"

    def get(self, request):
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        print("Cart Home", cart_obj)
        context = {
            "cart_obj": cart_obj,
        }
        return render(request,"carts/home.html", context)

def cart_update(request, *args, **kwargs):
    product_id = request.POST.get('product_id', None)
    product_quantity = request.POST.get('product_quantity', None)
    cart_item_update = request.POST.get('cart_item_update', False)
    cart_item_remove = request.POST.get('cart_item_remove', False)
    cart_item_add = request.POST.get('cart_item_add', False)

    product_obj = Product.objects.get(id=product_id)
    print("product_obj", product_obj)

    if product_obj:
        cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_obj=product_obj, product_quantity=product_quantity)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        print("product is not None?", product_obj)
        print("cart_item_obj is not None?", cart_item_obj)

        if cart_item_obj in cart_obj.cart_items.all() and cart_item_remove:
            print("cart_item_removed")
            cart_obj.cart_items.remove(cart_item_obj)

        if cart_item_obj in cart_obj.cart_items.all() and cart_item_update:
            print("cart_item_updated")
            cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_obj=product_obj, product_quantity=product_quantity)
        
        if cart_item_add:
            print("cart_item_added")
            cart_obj.cart_items.add(cart_item_obj)

        print("cart_item_update is: ", cart_item_update)
        print("cart_item_remove is: ", cart_item_remove)
        print("cart_item_add is: ", cart_item_add)

        request.session['cart_items'] = cart_obj.cart_items.count()
    return redirect("cart:home")

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.cart_items.count() == 0:
        redirect("cart:home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    print(order_obj)
    return render(request, "carts/checkout.html",{"object": order_obj})