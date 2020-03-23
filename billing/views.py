from django.shortcuts import render

def billing_default_page(request):
    context = {
        "title": "Billing Home Page",
        "page_header": "Billing",
        }
        
    if request.user.is_authenticated:
        context["content"] = "billing_default_page"
    else:
        context["content"] = "No billing info found - Please log in:"
        
    return render(request, "billing/billing-home.html", context)
