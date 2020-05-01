from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.http import Http404
from .models import Product


class ProductDefaultView(TemplateView):
    template_name = "products/products-home.html"
    queryset = Product.objects.all()
    
    def get(self, request):
        active_products = Product.objects.all().filter(active=True)
        context = {
            "title": "Products Home Page",
            "page_header": "Products",
            "products": active_products
            }
        return render(request, self.template_name, context)

class ProductDetailView(DetailView):
    template_name="products/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)        
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('id')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("product doesn't exist")
        return instance