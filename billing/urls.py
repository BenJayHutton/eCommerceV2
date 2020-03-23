from django.conf.urls import url
from .views import billing_default_page

urlpatterns = [
    url(r'^$', billing_default_page, name='default_home'),
]