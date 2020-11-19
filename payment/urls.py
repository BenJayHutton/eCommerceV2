from django.conf.urls import url
from django.urls import path, re_path

from .views import PaymentHome, Paypal

urlpatterns = [
    url(r'^$', PaymentHome.as_view(), name='home'),
    url(r'^paypal/$', Paypal.as_view(), name='paypal'),
]