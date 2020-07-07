from django.conf.urls import url
from django.urls import path, re_path

from .views import (
    ProductListView,
    ProductDetailSlugView,
)

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]