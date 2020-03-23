from django.shortcuts import render

def orders_default_page(request):
    context = {
        "title": "Orders Home Page",
        "page_header": "Orders",
        "content": "orders_default_page",
        }
        
    if request.user.is_authenticated:
        context["content"] = "orders_default_page"
    else:
        context["content"] = "No orders found - Please log in:"
        
    return render(request, "orders/orders-home.html", context)
