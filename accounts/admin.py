from django.contrib import admin

from .models import User, UserBillingAddress, UserShippingAddress, GuestEmail

admin.site.register(GuestEmail)
admin.site.register(User)
admin.site.register(UserBillingAddress)
admin.site.register(UserShippingAddress)