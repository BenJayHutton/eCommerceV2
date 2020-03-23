from django.shortcuts import render

def billing_default_page(request):
    context = {
        "title": "Billing Home Page",
        "page_header": "Billing",
        "content": "billing_default_page",
        }
    return render(request, "billing/billing-home.html", context)
