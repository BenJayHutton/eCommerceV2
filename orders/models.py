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

from eCommerce.utils import unique_order_id_generator
from products.models import Product
from carts.models import Cart
from billing.models import BillingProfile

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)
    

class Order(models.Model):
    billing_profile     = models.ForeignKey(BillingProfile, null=True, blank=True, on_delete=models.CASCADE)
    order_id            = models.CharField(max_length=120, unique=True, blank=True, null=True)
    cart                = models.ForeignKey(Cart, default=None, blank=True, on_delete=models.CASCADE)    
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total      = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    tax                 = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    total         = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    active              = models.BooleanField(default=True)
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    '''
    
    shipping_address    = models.ForeignKey(Address, default=None, blank=True, on_delete=models.CASCADE)
    billing_address     = models.ForeignKey(Address,default=None, blank=True, on_delete=models.CASCADE)
    '''

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = float(self.cart.subtotal)
        shipping_total = float(self.shipping_total)
        new_total = cart_total + shipping_total
        self.total = new_total
        self.save()
        return new_total


    def new_or_get_order(self, *args, **kwargs):
        product_id = kwargs['product_id']
        product_qty = kwargs['product_qty']
        session_order_id = kwargs['session_order_id']

        test_obj = Order(order_id = session_order_id)
        test_obj.save()
        print("shipping total:", test_obj.shipping_total)

        obj = Order.objects.filter(order_id__exact=1)
        
        
    
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id, sender=Order)

def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total  = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total, sender=Cart)


def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order, sender=Order)