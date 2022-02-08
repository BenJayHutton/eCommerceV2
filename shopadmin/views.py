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
        context = {}
        return render(request, "shopadmin/home.html", context)
