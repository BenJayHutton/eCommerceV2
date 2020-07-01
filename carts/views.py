from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpRequest

from products.models import Product
from .models import Cart, CartItem

class CartHome(ListView):
    template_name = "carts/list.html"
    
    product_obj = None
    quantity = None
    price = None
    cart_item = None

    def cart_create(user=None):
        cart_obj = Cart.objects.create(user=None)
        print("new cart created")
        return cart_obj

    def get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            cart_obj = qs.first()
            print('cart exists')
        else:
            cart_obj = cart_create()
        context = {}        
        return render(request,"carts/list.html", context)
    

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')
        
        if product_id is not None:
            cart_obj = CartItem.objects.create_cart_item(product_id=product_id, product_quantity=product_quantity)
            print(cart_obj)           
        
        context = {
            "cart_obj_id": cart_obj,
            "product_title": cart_obj.product.title,
            "product_quantity": product_quantity,
            "item_price": item_price,
            "total": total,
        }
        return render(request,"carts/list.html", context)