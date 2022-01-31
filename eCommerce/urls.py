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
from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

from .views import about_page, contact_page, DefaultHomePage
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from orders.views import LibraryView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', DefaultHomePage.as_view(display_name="home"), name='home'),
    re_path(r'^about/$', about_page, name='about'),
    re_path('admin/', admin.site.urls),
    re_path(r'^account/', include(("accounts.urls", "accounts"), namespace='account')),
    re_path(r'^accounts/', include(("accounts.urls", "accounts"), namespace='accounts')),
    re_path(r'^accounts/', include("accounts.password.urls")),
    re_path(r'^analytics/', include(("analytics.urls", "analytics"), namespace='analytics')),
    re_path(r'^billing/', include(("billing.urls", "billing"), namespace='billing')),
    re_path(r'^blog/', include(("blog.urls", "blog"), namespace='blog')),
    re_path(r'^cart/', include(("carts.urls", "carts"), namespace='cart')),
    re_path(r'^carts/', include(("carts.urls", "carts"), namespace='carts')),
    re_path(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    re_path(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    re_path(r'^contact/$', contact_page, name='contact'),
    re_path(r'^library/$', LibraryView.as_view(), name='library'),
    re_path(r'^marketing/', include(("marketing.urls", "marketing"), namespace='marketing')),
    re_path(r'^orders/', include(("orders.urls", "orders"), namespace='orders')),
    re_path(r'^products/', include(("products.urls", "products"), namespace='products')),
    re_path(r'^payment/', include(("payment.urls", "payment"), namespace='payment')),
    re_path(r'^search/', include(("search.urls", "search"), namespace='search')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
