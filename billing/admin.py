from django.contrib import admin

from .models import BillingProfile, Card, Charge


@admin.register(BillingProfile)
class BillingProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__email', 'customer_id']

    class Meta:
        model = BillingProfile


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    search_fields = ['billing_profile__user__email', 'stripe_id']

    class Meta:
        model = Card


@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    search_fields = ['billing_profile__user__email', 'stripe_id']

    class Meta:
        model = Charge
