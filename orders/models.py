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

from addresses.models import Address
from billing.models import BillingProfile
from carts.models import Cart
from products.models import Product


ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):
        qs = self.get_queryset().filter(billing_profile=billing_profile, cart=cart_obj, active = True, status='created')
        if qs.count() == 1:
            created = False
            obj = qs.first()
        else:
            obj  = self.model.objects.create(billing_profile=billing_profile, cart=cart_obj)
            created = True
        return obj
    

class Order(models.Model):
    billing_profile     = models.ForeignKey(BillingProfile, null=True, blank=True, on_delete=models.CASCADE)
    order_id            = models.CharField(max_length=120, unique=True, blank=True, null=True)
    shipping_address    = models.ForeignKey(Address, related_name=
    'shipping_address', null=True, blank=True, on_delete=models.CASCADE)
    billing_address     = models.ForeignKey(Address,null=True, related_name=
    'billing_address', blank=True, on_delete=models.CASCADE)
    cart                = models.ForeignKey(Cart, default=None, blank=True, on_delete=models.CASCADE)    
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total      = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    tax                 = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    active              = models.BooleanField(default=True)
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    
    
    objects = OrderManager()

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.subtotal
        shipping_total = self.shipping_total
        new_total = Decimal(cart_total) + Decimal(shipping_total)
        self.total = new_total
        print(self.total)
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
    
    def check_done(self):
        shipping_address_required = False #not self.cart.is_digital
        shipping_done = False
        
        if shipping_address_required and self.shipping_address:
            shipping_done = True
        elif shipping_address_required and not self.shipping_address:
            shipping_done = False
        else:
            shipping_done = True
        
        billing_profile = self.billing_profile
        billing_address = self.billing_address
        total = self.total
        if billing_profile and shipping_done and billing_address and total > 0:
            return True
        return False
    
    def update_purchases(self):
        for p in self.cart.cart_items.all():
            obj, create = ProductPurchase.objects.get_or_create(
                order_id = self.order_id,
                product = p,
                billing_profile= self.billing_profile,
            )
        return ProductPurchase.objects.filter(order_id = self.order_id).count()

    def mark_paid(self):
        if self.status != 'paid':
            if self.check_done():
                self.status = "paid"
                self.save()
                #self.update_purchases()
        return self.status
        
        
    
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)

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