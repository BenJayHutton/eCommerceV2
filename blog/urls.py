from django.conf.urls import url

from .views import BlogListView

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='home'),
]
