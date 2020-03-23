from django.conf.urls import url
from .views import products_default_page

urlpatterns = [
    url(r'^$', products_default_page, name='default_home'),
]