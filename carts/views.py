from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic import TemplateView, DetailView, ListView
from django.http import HttpResponse, HttpRequest

from products.models import Product

class Cart(ListView):

    def update_cart(self, *args, **kwargs):
        print(kwargs, args)

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')
        product_obj = Product().get_by_id(product_id)
        print(product_obj.title)
        self.update_cart(product_id=product_id)
        return redirect("products:home")