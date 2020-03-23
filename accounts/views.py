from django.shortcuts import render

def accounts_default_page(request):
    context = {
        "title": "Accounts Home Page",
        "page_header": "Accounts",
        "content": "accounts_default_page",
        }
    return render(request, "accounts/accounts-home.html", context)
