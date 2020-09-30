from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.utils.http import is_safe_url

STRIPE_PUB_KEY = getattr(settings,"STRIPE_PUB_KEY",None)
STRIPE_SECRET_API_KEY = getattr(settings, "STRIPE_SECRET_API_KEY", None)

# class BillingDefaultPage(TemplateView):
#     template_name = "billing/billing-home.html"
    
#     def get(self, request):
#         context = {
#             "title": "Billing Home Page",
#             "page_header": "Billing",
#             }
            
#         if request.user.is_authenticated:
#             context["content"] = "billing_default_page"
#         else:
#             context["content"] = "No billing info found - Please log in:"
            
#         return render(request, self.template_name, context)

def pay_method_view(request):
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    
    context = {
        'publish_key': STRIPE_PUB_KEY,
        'next_url': next_url
        }

    return render(request, 'billing/payment-method.html', context)

def pay_method_createview(request):
    print("request.POST",request.POST)
    if request.method == "POST" and request.is_ajax():
        print(request.POST)
        return JsonResponse({"message": "Success! your card was added"})
    return HttpResponse("404...not found", status=404)