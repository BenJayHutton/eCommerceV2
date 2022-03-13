from django.urls import path, re_path


from .views import (
    SalesView,
    SalesAjaxView,
    OrderView,
    ObjectViewList,
)

urlpatterns = [
    re_path(r'^orders/$', OrderView.as_view(), name='orders'),
    re_path(r'^sales/$', SalesView.as_view(), name='sales-analytics'),
    re_path(r'^sales/data/$', SalesAjaxView.as_view(), name='sales-data'),
    path('data/', ObjectViewList.as_view(), name='analytics-data'),

]
