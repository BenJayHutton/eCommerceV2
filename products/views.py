from django.http import Http404
from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView

from analytics.mixins import ObjectViewedMixin
from carts.models import Cart, CartItem

from .models import Product

class ProductListView(ListView):
    template_name = "products/list.html"
    
    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        cart_item_id = {}
        context['cart_obj'] = cart_obj
        context['cart_item_id'] = cart_item_id
        
        cart_item_obj = []       
        for items in cart_obj.cart_items.all():
            cart_item_obj.append(items.product)
            cart_item_id[items.product] = int(items.id)
            
        context['cart_item_obj'] = cart_item_obj
        print("cart_item_obj", cart_item_obj)
        print("items: ", cart_item_id, type(cart_item_id))
        return context
        

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailSlugView(ObjectViewedMixin, DetailView):
    queryset = Product.objects.all()
    template_name="products/detail.html"

    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get('slug')
        
        cart_obj, new_cart_obj = Cart.objects.new_or_get(request)
        cart_item_id = {}
        cart_item_obj = []       
        for items in cart_obj.cart_items.all():
            cart_item_obj.append(items.product)
            cart_item_id[items.product] = int(items.id)
        

        try:
            product_obj = Product.objects.get(slug=slug)
        except:
            product_obj = None
        
        for items in cart_obj.cart_items.all():
            cart_item_id[items.product] = int(items.id)
        
        context = {
            'cart_obj': cart_obj,
            'product_obj': product_obj,
            'cart_item_id': cart_item_id,
            'cart_item_obj': cart_item_obj,
            }
        return context

    
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.get(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Product not found")
        
        return instance