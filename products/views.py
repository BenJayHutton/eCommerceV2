from django.http import Http404
from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView

from carts.models import Cart, CartItem
from .models import Product


class ProductListView(ListView):
    template_name = "products/list.html"
    queryset = Product.objects.all().active()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name="products/detail.html"

    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get('slug')
        product_id = kwargs.get('object')
        print("kwargs", kwargs)
        print("Slug: ", slug)

        cart_obj, new_cart_obj = Cart.objects.new_or_get(request)
        try:
            product_obj = Product.objects.get(slug=slug)
        except:
            product_obj = None
        
        print("product_obj", product_obj)
        context = {
            'cart': cart_obj,
            'product_obj': product_obj,            
            }
        return context

    def post(self, request, *args, **kwargs):
        try:
            cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_id = product_obj.id)
            print("product in cart item: ",cart_item_obj.product)
        except:
            cart_item_obj = None
        context = {
            'product_obj': product_obj,            
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