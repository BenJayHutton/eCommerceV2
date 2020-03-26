from django.conf.urls import url
from .views import BillingDefaultPage

urlpatterns = [
    url(r'^$', BillingDefaultPage.as_view(), name='default_home'),
]