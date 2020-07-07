from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpRequest

from products.models import Product
from .models import Cart, CartItem

class CartHome(ListView):
    template_name = "carts/list.html"

    def get(self, request):
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context = {
            "cart_obj": cart_obj,
        }
        return render(request,"carts/list.html", context)
    

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id', None)
        product_quantity = request.POST.get('product_quantity')
        cart_item_obj = CartItem.objects.new_or_get(request, product_id=product_id, product_quantity=product_quantity)        
        print(cart_item_obj)
            
        context = {
            "cart_item_obj": cart_item_obj,
        }
        return render(request,"carts/list.html", context)

def cart_update(request, *args, **kwargs):
    product_id = kwargs.get('product_id', None)
    product_quantity = kwargs.get('product_quantity', None)
    cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_id=product_id, product_quantity=product_quantity)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.cart_items.add(cart_item_obj)
    
    return redirect("cart:cart")