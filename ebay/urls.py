from django.conf.urls import url

from .views import (
EbaySearchListing
)

urlpatterns = [
    url(r'^$', EbaySearchListing.as_view(), name='home'),
]
