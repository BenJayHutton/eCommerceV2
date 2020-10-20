from django.conf.urls import url
from django.contrib.auth.views import LogoutView 
from .views import (
    Accounts, 
    LoginView, 
    RegisterView, 
    logout_view, 
    guest_register_page, 
    AccountEmailActivateView,
    )

urlpatterns = [
    url(r'^$', Accounts.as_view(), name='home'),
    url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),
    url(r'^email/resend-activation/$', AccountEmailActivateView.as_view(), name='resend-activation'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/guest/$', guest_register_page, name='guest_register'),    
    url(r'^logout/$', logout_view, name='logout'),
]