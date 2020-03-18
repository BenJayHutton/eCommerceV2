from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class BillingManagerQuerySet(models.query.QuerySet):
    pass

class BillingProfileManager(models.Manager):
    pass
    
class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=120, null=True, blank=True)
    # customer_id in payment processer
    
    objects = BillingProfileManager()


class InvoiceManagerQuerySet(models.query.QuerySet):
    pass

class InvoiceProfileManager(models.Manager):
    pass
    
class Invoice(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    invoice_no  = models.IntegerField(null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    
    objects = InvoiceProfileManager()