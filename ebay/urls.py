from django.urls import path
from .views import (
    EbaySearchListing,
    EbayFindingApi,
)

urlpatterns = [
    path(r'', EbaySearchListing.as_view(), name='home'),
    path(r'findingApi/<search>/', EbayFindingApi.as_view(), name='home'),
]
