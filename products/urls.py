from django.conf.urls import url
from .views import ProductDefaultView

urlpatterns = [
    url(r'^$', ProductDefaultView.as_view(), name='default_home'),
]