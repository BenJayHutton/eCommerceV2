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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', DefaultHomePage.as_view(display_name="home"), name='home'),
    url(r'^$', DefaultHomePage.as_view(display_name="about"), name='about'),
    url(r'^accounts/', include(("accounts.urls", "accounts"), namespace='accounts')),
    url(r'^billing/', include(("billing.urls", "billing"), namespace='billing')),
    url(r'^cart/', include(("carts.urls", "carts"), namespace='cart')),
    url(r'^carts/', include(("carts.urls", "carts"), namespace='carts')),
    url(r'^orders/', include(("orders.urls", "orders"), namespace='orders')),
    url(r'^products/', include(("products.urls", "products"), namespace='products')),
]
