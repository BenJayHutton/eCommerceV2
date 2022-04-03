from django.urls import re_path
from .views import pay_method_view, pay_method_createview

urlpatterns = [
    re_path(r'^payment-method/$', pay_method_view, name='billing-payment-method'),
    re_path(r'^payment-method/create/$', pay_method_createview, name='billing-payment-method-endpoint'),
]
