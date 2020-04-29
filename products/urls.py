from django.conf.urls import url
from django.urls import path, re_path

from .views import ProductDefaultView, ProductDetailView

urlpatterns = [
    url(r'^$', ProductDefaultView.as_view(), name='default_home'),
    re_path(r'^(?P<id>\d+)/?$', ProductDetailView.as_view(), name='detail'),
]