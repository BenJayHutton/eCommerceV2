from django.conf.urls import url, re_path
from .views import (
    CartHome, 
    cart_update, 
    checkout_home,
    checkout_done_view,
    )

urlpatterns = [
    url(r'^$', CartHome.as_view(), name='home'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^checkout/success/$', checkout_done_view, name='success'),
    url(r'^update/$', cart_update, name='update'),
]