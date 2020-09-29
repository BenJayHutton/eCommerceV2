from django.conf.urls import url
from .views import pay_method_view, pay_method_createview

urlpatterns = [
    #url(r'^$', BillingDefaultPage.as_view(), name='default_home'),
    url(r'^payment-method/$', pay_method_view, name='billing-payment-method'),
    url(r'^payment-method/create/$', pay_method_createview, name='billing-payment-method-endpoint'),
]