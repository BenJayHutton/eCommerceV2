from django.conf.urls import url
from .views import orders_default_page

urlpatterns = [
    url(r'^$', orders_default_page, name='default_home'),
]