from django.conf.urls import url
from .views import Accounts

urlpatterns = [
    url(r'^$', Accounts.as_view(), name='home'),
]