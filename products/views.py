from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
#from django.views import ListView
from django.http import Http404
from .models import Product


class ProductDefaultView(ListView):
    template_name = "products/products-home.html"
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    template_name="products/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)        
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('id')
        product = Product.objects.get_by_id(pk)
        if product is None:
            raise Http404("product doesn't exist")
        return product