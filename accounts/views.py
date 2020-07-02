from django.shortcuts import render
from django.views.generic import TemplateView


class Accounts(TemplateView):
    template_name = "accounts/home.html"
    
    def get(self, request):
        context = {
            "title": "Accounts Home Page",
            "page_header": "Accounts",
            }
        return render(request, self.template_name, context)