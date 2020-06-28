from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpRequest

from products.models import Product
from .models import Cart

class Cart(ListView):
    template_name = "carts/list.html"
    queryset = Cart.objects.all()

    def get(self, request):
        context = {}        
        return render(request,"carts/list.html", context)