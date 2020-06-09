from django.conf.urls import url
from .views import OrderDefaultView

urlpatterns = [
    url(r'^$', OrderDefaultView.as_view(), name='default_home'),
    url(r'^$', OrderDefaultView.as_view(), name='update_order'),
]