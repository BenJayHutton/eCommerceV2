from django.contrib import admin

from .models import BillingProfile, Card, Charge


class BillingAdmin(admin.ModelAdmin):
    search_fields = ['user__email', 'customer_id']

    class Meta:
        model = BillingProfile


class CardAdmin(admin.ModelAdmin):
    search_fields = ['billing_profile__user__email', 'stripe_id']

    class Meta:
        model = Card


class ChargeAdmin(admin.ModelAdmin):
    search_fields = ['billing_profile__user__email', 'stripe_id']

    class Meta:
        model = Charge


admin.site.register(BillingProfile, BillingAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Charge, ChargeAdmin)
