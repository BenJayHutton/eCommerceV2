from django.conf.urls import url
from .views import CartHome, cart_update

urlpatterns = [
    url(r'^$', CartHome.as_view(), name='cart'),
    url(r'^update/$', cart_update, name='update'),
]