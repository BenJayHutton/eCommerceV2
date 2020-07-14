from django.conf.urls import url
from .views import (
    CartHome, 
    cart_update, 
    checkout_home,
    )

urlpatterns = [
    url(r'^$', CartHome.as_view(), name='home'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', cart_update, name='update'),
]