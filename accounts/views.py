from django.shortcuts import render

def accounts_default_page(request):
    context = {
        "title": "Accounts Home Page",
        "page_header": "Accounts",
        }
        
    if request.user.is_authenticated:
        context["content"] = "accounts_default_page"
    else:
        context["content"] = "No account info found - Please log in:"
        
    return render(request, "accounts/accounts-home.html", context)
