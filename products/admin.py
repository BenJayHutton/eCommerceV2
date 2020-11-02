from django.contrib import admin

from .models import Product, ItemImage, ItemTag, ProductFile

class ProductFileInline(admin.TabularInline):
    model= ProductFile
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    inlines = [ProductFileInline]
    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin,)
admin.site.register(ItemImage)
admin.site.register(ItemTag)
