from django.shortcuts import render
from django.views.generic import TemplateView


class OrderDefaultView(TemplateView):
    template_name = "orders/orders-home.html"
    
    def get(self, request):
        context = {
            "title": "Orders Home Page",
            "page_header": "Orders",
            }
            
        if request.user.is_authenticated:
            context["content"] = "orders_default_page"
        else:
            context["content"] = "No orders found - Please log in:"
            
        return render(request, self.template_name , context)
