from django.conf.urls import url
from .views import Cart, update_cart

urlpatterns = [
    url(r'^$', Cart.as_view(), name='cart'),
    url(r'^$', update_cart, name='update_cart'),
]