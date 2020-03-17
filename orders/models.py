from decimal import Decimal
import datetime
from django.conf import settings
from django.db import models
from django.db.models import Count, Sum, Avg
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils import timezone

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

class OrderManagerQuerySet(models.query.QuerySet):
    pass
    
class OrderManager(models.Manager):
    pass

class Order(models.Model):
    order_id            = models.CharField(max_length=120, blank=True)
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
    
    objects = OrderManager()
    
    pass