from django.conf.urls import url

from .views import (
    SalesView,
    SalesAjaxView,
    OrderView,
)

urlpatterns = [
    url(r'^orders/$', OrderView.as_view(), name='orders'),
    url(r'^sales/$', SalesView.as_view(), name='sales-analytics'),
    url(r'^sales/data/$', SalesAjaxView.as_view(), name='sales-data'),
]
