from django.contrib import admin

from .models import Order, ProductPurchase

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['order_id', 'billing_profile__email']
    list_display = ['order_id', 'billing_profile', 'status']
    list_filter = ('active', 'status')

    class Meta:
        model = Order



@admin.register(ProductPurchase)
class ProductPurchaseAdmin(admin.ModelAdmin):
    search_fields = ['order_id','billing_profile__email','product__title','refunded']
    list_display = ['order_id','billing_profile','product','refunded'  ]
    
