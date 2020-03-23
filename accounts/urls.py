from django.conf.urls import url
from .views import accounts_default_page

urlpatterns = [
    url(r'^$', accounts_default_page, name='default_home'),
]