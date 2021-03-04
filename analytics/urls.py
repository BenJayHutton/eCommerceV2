from django.conf.urls import url
from django.urls import path

from .views import (
    SalesView,
    SalesAjaxView,
    OrderView,
    ObjectViewList,
)

urlpatterns = [
    url(r'^orders/$', OrderView.as_view(), name='orders'),
    url(r'^sales/$', SalesView.as_view(), name='sales-analytics'),
    url(r'^sales/data/$', SalesAjaxView.as_view(), name='sales-data'),
    path('data/', ObjectViewList.as_view(), name='analytics-data'),

]
