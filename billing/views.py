from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.utils.http import is_safe_url

import stripe

from .models import BillingProfile, Card


STRIPE_PUB_KEY = getattr(settings,"STRIPE_PUB_KEY",None)
STRIPE_SECRET_API_KEY = getattr(settings, "STRIPE_SECRET_API_KEY", None)
stripe.api_key = STRIPE_SECRET_API_KEY
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
    if request.user.is_authenticated:
        billing_profile = request.user.billingprofile
        my_customer_id = billing_profile.customer_id
    
    
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

    if not billing_profile:
        return redirect("/cart")
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
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message":"Cannot find this user"}, status=401)

        token = request.POST.get("token")

        if token is not None:
            # customer = stripe.Customer.retrieve(billing_profile.customer_id)
            # card_response = customer.sources.create(source=token)
            #new_card_obj = Card.objects.add_new(billing_profile, card_response)
            new_card_obj = Card.objects.add_new(billing_profile, token)
            print("new_card_obj",new_card_obj)
        return JsonResponse({"message": "Success! your card was added"})
    return HttpResponse("401...not found", status=401)