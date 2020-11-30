from django.conf.urls import url

from .views import PaymentHome, Paypal

urlpatterns = [
    url(r'^$', PaymentHome.as_view(), name='home'),
    url(r'^paypal/$', Paypal.as_view(), name='paypal'),
]
