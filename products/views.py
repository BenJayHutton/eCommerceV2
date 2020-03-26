from django.shortcuts import render
from django.views.generic import TemplateView


class ProductDefaultView(TemplateView):
    template_name = "products/products-home.html"
    
    def get(self, request):
        context = {
            "title": "Products Home Page",
            "page_header": "Products",
            "content": "No products so far",
            }
        return render(request, self.template_name, context)
