from django.http import Http404
from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView

from carts.models import Cart, CartItem
from .models import Product

class ProductListView(ListView):
    template_name = "products/list.html"
    queryset = Product.objects.all().active()

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all().active()
        cart_obj, new_cart_obj = Cart.objects.new_or_get(request)
        print(queryset)
        context = {
            'object_list': queryset,
            'cart_obj':cart_obj,

        }
        return render(request,"products/list.html", context)


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
        cart_item_obj, new_item_obj = CartItem.objects.new_or_get(request, product_obj=product_obj)
        print("product obj", product_obj)
        
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
            print("product in cart item: ",cart_item_obj.product)
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