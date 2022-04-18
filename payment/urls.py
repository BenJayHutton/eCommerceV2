from django.urls import re_path

from .views import PaymentHome, Paypal, Stripe

urlpatterns = [
    re_path(r'^$', PaymentHome.as_view(), name='home'),
    re_path(r'^paypal/$', Paypal.as_view(), name='paypal'),
    re_path(r'^stripe/$', Stripe.as_view(), name='stripe'),
]
