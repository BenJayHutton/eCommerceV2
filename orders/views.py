from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpRequest

from .models import Order
from products.models import Product


class OrderHome(TemplateView):
    template_name = "orders/orders-home.html"
    session_id = SessionStore()
    
    def get(self, request, *args, **kwargs):
        context = {
            "title": "Orders Home Page",
            "page_header": "Orders",
            }
            
        if request.user.is_authenticated:
            context["content"] = "orders_default_page"
        else:
            context["content"] = "No orders found - Please log in:"
        return render(request, self.template_name , context)

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')
        product_obj = Product().get_by_id(product_id)
        return HttpResponse(product_obj.title)
        
    def add_to_order(self, *args, **kwargs):
        return True
