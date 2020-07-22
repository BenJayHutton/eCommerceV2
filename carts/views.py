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

    cart_item_id = request.POST.get('cart_item_id', None)
    cart_item_update = request.POST.get('cart_item_update', False)
    cart_item_remove = request.POST.get('cart_item_remove', False)
    cart_item_add = request.POST.get('cart_item_add', False)
    product_id = request.POST.get("product_id", None)
    product_quantity = request.POST.get('product_quantity', None)
    try:
        product_obj = Product.objects.get(id=product_id)
    except:
        product_obj = False
    
    print("-----------------------")
    print("| cart_item_id", cart_item_id)
    print("| cart_item_update", cart_item_update)
    print("| cart_item_remove", cart_item_remove)
    print("| cart_item_add", cart_item_add)
    print("| product_id", product_id)
    print("| product_quantity", product_quantity)
    print("| product_obj", product_obj)
    print("-----------------------")

    if product_obj:
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if cart_item_remove:
            cart_item_obj = CartItem.objects.get(id=cart_item_id)
            cart_obj.cart_items.remove(cart_item_obj)
            print("cart_item_obj", cart_item_obj)
            print("cart_item_removed")

        if cart_item_update:
            update_cart_total = Cart.objects.calculate_cart_total(request, cart_obj=cart_obj)
            cart_item_obj = CartItem.objects.get(id=cart_item_id)
            print("cart_item_updat:", cart_item_obj, "product_obj:", product_obj, "qty", cart_item_obj.quantity)
            if int(product_quantity) != int(cart_item_obj.quantity):
                cart_item_obj.quantity = product_quantity
                cart_item_obj.save()
                cart_total = Cart.objects.calculate_cart_total(request, cart_obj=cart_obj)
                print("quantity updated")
            
        
        if cart_item_add:
            cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_obj=product_obj, product_quantity=product_quantity)
            cart_obj.cart_items.add(cart_item_obj)
            print("cart_item_obj", cart_item_obj)
            print("product_obj", product_obj)
            print("cart_item_added", cart_obj, "=>", cart_item_obj)
        
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