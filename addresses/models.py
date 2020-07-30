from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPE = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

LIST_OF_COUNTRIES = (
    ('uk', 'United Kingdom'),
    ('usa', 'United States of America')
)

class Address(models.Model):
    billing_profile  = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type   = models.CharField(max_length=12, choices=ADDRESS_TYPE)
    address_line_1   = models.CharField(max_length=120)
    address_line_2   = models.CharField(max_length=120, null=True, blank=True)
    city             = models.CharField(max_length=120)    
    state            = models.CharField(max_length=120)
    postal_code      = models.CharField(max_length=120)
    country          = models.CharField(max_length=120, choices=LIST_OF_COUNTRIES, default='uk')

    def __str__(self):
        return str(self.billing_profile)