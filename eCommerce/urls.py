"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from .views import about_page, contact_page, DefaultHomePage
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from accounts.views import LoginView
from orders.views import LibraryView


urlpatterns = [
    url(r'^$', DefaultHomePage.as_view(display_name="home"), name='home'),
    url(r'^about/$', about_page, name='about'),
    path('admin/', admin.site.urls),
    url(r'^account/', include(("accounts.urls", "accounts"), namespace='account')),
    url(r'^accounts/', include(("accounts.urls", "accounts"), namespace='accounts')),
    url(r'^accounts/', include("accounts.password.urls")),
    url(r'^billing/', include(("billing.urls", "billing"), namespace='billing')),
    url(r'^cart/', include(("carts.urls", "carts"), namespace='cart')),
    url(r'^carts/', include(("carts.urls", "carts"), namespace='carts')),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^marketing/', include(("marketing.urls", "marketing"), namespace='marketing')),
    url(r'^orders/', include(("orders.urls", "orders"), namespace='orders')),
    url(r'^products/', include(("products.urls", "products"), namespace='products')),
    url(r'^search/', include(("search.urls", "search"), namespace='search')),
]