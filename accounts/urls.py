from django.urls import re_path

from products.views import UserProductHistoryView

from .views import (
    Accounts, 
    LoginView, 
    RegisterView, 
    logout_view, 
    GuestRegisterView, 
    AccountEmailActivateView,
    UserDetailUpdateView,
    )

urlpatterns = [
    re_path(r'^$', Accounts.as_view(), name='home'),
    re_path(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    re_path(r'^history/products/$', UserProductHistoryView.as_view(), name='user-product-history'),
    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),
    re_path(r'^email/resend-activation/$', AccountEmailActivateView.as_view(), name='resend-activation'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^register/$', RegisterView.as_view(), name='register'),
    re_path(r'^register/guest/$', GuestRegisterView.as_view(), name='guest_register'),    
    re_path(r'^logout/$', logout_view, name='logout'),
]
