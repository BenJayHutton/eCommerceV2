from django.conf.urls import url
from .views import CartHome

urlpatterns = [
    url(r'^$', CartHome.as_view(), name='cart'),
]