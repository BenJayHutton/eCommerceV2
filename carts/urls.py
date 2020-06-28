from django.conf.urls import url
from .views import Cart

urlpatterns = [
    url(r'^$', Cart.as_view(), name='home'),
]