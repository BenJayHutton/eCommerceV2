from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from carts.models import Cart

class SearchProductView(ListView):
    template_name="search/view.html"
    

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        request = self.request
        query = request.GET.get('q')
        cart_obj, new_cart_obj = Cart.objects.new_or_get(request)
        context['query'] = query
        context['cart_obj'] = cart_obj
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()