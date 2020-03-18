from django.contrib import admin

from .models import BillingProfile, Invoice

admin.site.register(BillingProfile)
admin.site.register(Invoice)
