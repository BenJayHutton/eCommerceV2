from django.conf.urls import url

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
    url(r'^$', Accounts.as_view(), name='home'),
    url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    url(r'^history/products/$', UserProductHistoryView.as_view(), name='user-product-history'),
    url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),
    url(r'^email/resend-activation/$', AccountEmailActivateView.as_view(), name='resend-activation'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/guest/$', GuestRegisterView.as_view(), name='guest_register'),    
    url(r'^logout/$', logout_view, name='logout'),
]