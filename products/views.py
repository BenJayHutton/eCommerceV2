from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView, View

from analytics.mixins import ObjectViewedMixin
from orders.models import ProductPurchase
from carts.models import Cart, CartItem

from .models import Product, ProductFile

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
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().active()

class UserProductHistoryView(LoginRequiredMixin, ListView):
    template_name = "products/user-history.html"
    
    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(UserProductHistoryView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        cart_item_id = {}
        context['cart_obj'] = cart_obj
        context['cart_item_id'] = cart_item_id        
        cart_item_obj = []       
        for items in cart_obj.cart_items.all():
            cart_item_obj.append(items.product)
            cart_item_id[items.product] = int(items.id)            
        context['cart_item_obj'] = cart_item_obj
        return context
        

    def get_queryset(self, *args, **kwargs):
        request = self.request
        views = request.user.objectviewed_set.by_model(Product, model_queryset=False)
        return views
import os
from wsgiref.util import FileWrapper
from django.conf import settings
from mimetypes import guess_type

class ProductDownloadView(View):
        def get (self, request, *args, **kwargs):
            slug = kwargs.get('slug')
            pk = kwargs.get('pk')
            downloads_qs = ProductFile.objects.filter(pk=pk, product__slug=slug)
            if downloads_qs.count() !=1:
                raise Http404("Download not found")
            download_obj = downloads_qs.first()
            # permission check
            can_download = False
            user_ready = True

            if download_obj.user_required:
                if not request.user.is_authenticated:
                    user_ready = False
                else:
                    can_download = False

            purchased_products = Product.objects.none()
            if download_obj.free:
                can_download = True
                user_ready = True
            else:
                purchased_products = ProductPurchase.objects.products_by_request(request)
                if download_obj.product in purchased_products:
                    can_download = True
            
            if not can_download or not user_ready:
                messages.error(request, "You don't have access to download media")
                return redirect(download_obj.get_default_url())

            aws_filepath = download_obj.generate_download_url()
            print(aws_filepath)
            return HttpResponseRedirect(aws_filepath)

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