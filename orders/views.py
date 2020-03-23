from django.shortcuts import render

def orders_default_page(request):
    context = {
        "title": "Orders Home Page",
        "page_header": "Orders",
        "content": "orders_default_page",
        }
    return render(request, "orders/orders-home.html", context)
