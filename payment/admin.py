from django.contrib import admin
from .models import Payment, PaypalPaymentMethod, StripePaymentMethod

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['order', 'user__email', 'paypalOrderID', 'paypalPayerID']
    list_display = ['paymentMethod', 'order', 'is_paid']


@admin.register(PaypalPaymentMethod)
class PaypalPaymentAdmin(admin.ModelAdmin):
    search_fields = ['paypalOrderID', 'paypalPayerID']
    list_display = ['paypalOrderID']


@admin.register(StripePaymentMethod)
class StripePaymentAdmin(admin.ModelAdmin):
    search_fields = ['stripe_id']
    list_display = ['stripe_id', 'brand', 'exp_year', 'last4']
