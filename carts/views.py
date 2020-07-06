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
        cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_id=1)
        return render(request,"carts/list.html", {})
    

    def post(self, request, *args, **kwargs):
        '''
        updating cart:
            cart_item = CartItems.objects.create_cart_item(id=id_of_product)
            cart_obj, new_obj = Cart.objects.new_or_get(request)

        '''
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

def cart_update(request):
    product_id = 1
    cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.cart_items.add(cart_item_obj)
    
    return redirect("cart:cart")