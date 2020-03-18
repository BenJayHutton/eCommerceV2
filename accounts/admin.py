from django.contrib import admin

from .models import User, UserBillingAddress, UserShippingAddress

admin.site.register(User)
admin.site.register(UserBillingAddress)
admin.site.register(UserShippingAddress)