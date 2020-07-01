from django.conf.urls import url
from django.urls import path, re_path

from .views import (
    ProductListView, 
    ProductDetailView,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    ProductDetailSlugView,
)

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='home'),
    url(r'^(?P<id>\d+)/?$', ProductFeaturedListView.as_view(), name='featured'),
    url(r'^(?P<id>\d+)/?$', ProductFeaturedDetailView.as_view(), name='featureddetail'),
    url(r'^(?P<id>\d+)/?$', ProductDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detailSlugView'),
]