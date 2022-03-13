from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from accounts.models import *
from addresses.models import *
from billing.models import *
from carts.models import *
from orders.models import *
from payment.models import *
from products.models import *

class ShopAdminHome(LoginRequiredMixin, View):
    
    def get(self, request):
        orders_to_ship = Order.objects.to_ship
        refunded_orders = Order.objects.refunded_orders
        context = {
            'orders_to_ship': orders_to_ship,
            'refunded_orders': refunded_orders,
            }
        return render(request, "shopadmin/home.html", context)
