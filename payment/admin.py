from django.contrib import admin

from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['order', 'user__email', 'paypalOrderID', 'paypalPayerID']
    list_display = ('paymentMethod', 'order', 'is_paid')


admin.site.register(Payment, PaymentAdmin)
