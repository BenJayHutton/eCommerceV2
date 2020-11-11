from django.conf.urls import url
from django.urls import path, re_path

from .views import (
    SalesView,
    SalesAjaxView,
)

urlpatterns = [
    url(r'^sales/$', SalesView.as_view(), name='sales-analytics'),
    url(r'^sales/data/$', SalesAjaxView.as_view(), name='sales-data'),
]