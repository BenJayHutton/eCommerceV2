from django.contrib import admin

from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ['billing_profile__email', 'address_type', 'address_line_1', 'city', 'state', 'postal_code', 'country']
    list_display = ['billing_profile', 'address_type', 'address_line_1', 'city', 'state', 'postal_code', 'country']

    class Meta:
        model = Address