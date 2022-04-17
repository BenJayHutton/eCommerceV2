from django.contrib import admin

from .models import Product, ItemImage, Tag, ProductFile


class ProductFileInline(admin.TabularInline):
    model = ProductFile
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'slug', 'description']
    list_display = ['__str__', 'slug', 'quantity']
    inlines = [ProductFileInline]

    class Meta:
        model = Product


admin.site.register(Product,ProductAdmin,)
admin.site.register(ItemImage)
admin.site.register(Tag)
