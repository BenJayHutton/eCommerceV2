from django.http import Http404
from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView

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
        


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name="products/detail.html"

    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get('slug')
        product_slug = kwargs.get('object')
        try:
            product_obj = Product.objects.get(slug=slug)
        except:
            product_obj = None
        cart_obj, new_cart_obj = Cart.objects.new_or_get(request)
        cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request)
        
        context = {
            'cart_obj': cart_obj,
            'cart_item_obj': cart_item_obj,
            'product_obj': product_obj,            
            }
        return context

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id', None)
        product_quantity = request.POST.get('product_quantity',None)
        try:
            cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_id = product_obj.id, product_quantity=product_quantity)
        except:
            cart_item_obj = None
        context = {
            "cart_item_obj": cart_item_obj,
        }
        return redirect("cart:cart", context)

    
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
            raise Http404("...")
        return instance