from django.conf.urls import url
from .views import OrderHome

urlpatterns = [
    url(r'^$', OrderHome.as_view(), name='home'),
    url(r'^$', OrderHome.as_view(), name='update_order'),
]