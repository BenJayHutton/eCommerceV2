from django.shortcuts import render
from django.views.generic import TemplateView


class BillingDefaultPage(TemplateView):
    template_name = "billing/billing-home.html"
    
    def get(self, request):
        context = {
            "title": "Billing Home Page",
            "page_header": "Billing",
            }
            
        if request.user.is_authenticated:
            context["content"] = "billing_default_page"
        else:
            context["content"] = "No billing info found - Please log in:"
            
        return render(request, self.template_name, context)
