from django.urls import path
from .views import (
    EbaySearchListing,
)

urlpatterns = [
    path(r'', EbaySearchListing.as_view(), name='home'),
]
