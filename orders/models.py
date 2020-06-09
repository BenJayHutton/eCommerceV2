from decimal import Decimal
import datetime
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore
from django.db import models
from django.db.models import Count, Sum, Avg
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponse

from eCommerce.utils import random_string_generator
from products.models import Product

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


class OrderItem(models.Model):
    product     = models.ForeignKey(Product, default=None, blank=True, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=0, null=True)

    def new_or_get_order(self):
        return True
        
    def update_order(self):
        return True
    

class Order(models.Model):
    order_id            = models.CharField(max_length=120, unique=True, blank=True, null=True)
    OrderItem             = models.ManyToManyField(OrderItem, default=None, blank=True)
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total      = models.DecimalField(default=0.00, max_digits=3, decimal_places=2)
    tax                 = models.DecimalField(default=0.00, max_digits=3, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=3, decimal_places=2)
    active              = models.BooleanField(default=True)
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    '''
    billing_profile     = models.ForeignKey BillingProfile    
    shipping_address    = models.ForeignKey Address 
    billing_address     = models.ForeignKey Address
    cart                = models.ForeignKey Cart    
    '''

    def __str__(self):
        return self.order_id


    def new_or_get_order(self, *args, **kwargs):
        product_id = kwargs['product_id']
        product_qty = kwargs['product_qty']
        session_order_id = kwargs['session_order_id']

        test_obj = Order(order_id = session_order_id)
        test_obj.save()
        print("shipping total:", test_obj.shipping_total)

        obj = Order.objects.filter(order_id__exact=1)
        print(obj)

        print("product_id: ", product_id)
        print("product_qty: ", product_qty)
        print("session_order_id: ", session_order_id)
        
    
    def generate_order_id(self):
         return random_string_generator(120)