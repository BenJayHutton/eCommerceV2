from django.shortcuts import render
from django.views.generic import TemplateView


class AccountsDefaultPage(TemplateView):
    template_name = "accounts/accounts-home.html"
    
    def get(self, request):
        context = {
            "title": "Accounts Home Page",
            "page_header": "Accounts",
            }
    
        if request.user.is_authenticated:
            context["content"] = "accounts_default_page"
        else:
            context["content"] = "No account info found - Please log in:"

        return render(request, self.template_name, context)