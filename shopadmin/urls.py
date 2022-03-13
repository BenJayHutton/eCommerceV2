from django.urls import re_path

from .views import (
    ShopAdminHome,
)

urlpatterns = [
    re_path(r'^$', ShopAdminHome.as_view(), name='home'),
]