from django.http import Http404
from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"
    queryset = Product.objects.all().featured

class ProductFeaturedDetailView(DetailView):
    pass


class ProductListView(ListView):
    template_name = "products/list.html"
    queryset = Product.objects.all()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name="products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not found...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.get(slug=slug)
            instance = qs.first()
        except:
            raise Http404("...")
        return instance

class ProductDetailView(DetailView):
    template_name="products/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)        
        return context
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('id')
        qs = Product.objects.get_by_id(pk)
        if qs is None:
            raise Http404("product doesn't exist")
        else:
            return qs