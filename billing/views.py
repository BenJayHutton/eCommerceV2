from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme

import stripe

from .models import BillingProfile, Card

STRIPE_PUB_KEY = getattr(settings,"STRIPE_PUB_KEY",None)
STRIPE_SECRET_API_KEY = getattr(settings, "STRIPE_SECRET_API_KEY", None)
stripe.api_key = STRIPE_SECRET_API_KEY


def pay_method_view(request):
    if request.user.is_authenticated:
        billing_profile = request.user.billingprofile
        my_customer_id = billing_profile.customer_id

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

    if not billing_profile:
        return redirect("/cart")
    next_url = None
    next_ = request.GET.get('next')
    if url_has_allowed_host_and_scheme(next_, request.get_host()):
        next_url = next_
    
    context = {
        'publish_key': STRIPE_PUB_KEY,
        'next_url': next_url
        }

    return render(request, 'billing/payment-method.html', context)


def pay_method_createview(request):
    if request.method == "POST" and request.accepts('application/json'):
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message":"Cannot find this user"}, status=401)

        token = request.POST.get("token")

        if token is not None:
            new_card_obj = Card.objects.add_new(billing_profile, token)
        return JsonResponse({"message": "Success! your card was added"})
    return HttpResponse("401...not found", status=401)
