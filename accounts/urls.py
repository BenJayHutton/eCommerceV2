from django.conf.urls import url
from .views import AccountsDefaultPage

urlpatterns = [
    url(r'^$', AccountsDefaultPage.as_view(), name='default_home'),
]