from django.conf.urls import url
from django.contrib.auth.views import LogoutView 
from .views import Accounts, login_page, register_page, logout_view

urlpatterns = [
    url(r'^$', Accounts.as_view(), name='home'),
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
    url(r'^logout/$', logout_view, name='logout'),
]