from django.shortcuts import render

def products_default_page(request):
    context = {
        "title": "Products Home Page",
        "page_header": "Products",
        "content": "products_default_page",
        }
    return render(request, "products/products-home.html", context)
