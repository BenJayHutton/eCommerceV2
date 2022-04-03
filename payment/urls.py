from django.urls import re_path

from .views import PaymentHome, Paypal

urlpatterns = [
    re_path(r'^$', PaymentHome.as_view(), name='home'),
    re_path(r'^paypal/$', Paypal.as_view(), name='paypal'),
]
