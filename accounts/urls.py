from django.conf.urls import url
from django.contrib.auth.views import LogoutView 
from .views import Accounts, LoginView, RegisterView, logout_view, guest_register_page

urlpatterns = [
    url(r'^$', Accounts.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/guest/$', guest_register_page, name='guest_register'),    
    url(r'^logout/$', logout_view, name='logout'),
]