from django.contrib import admin
from .models import EbayAccount


@admin.register(EbayAccount)
class EbayAccountAdmin(admin.ModelAdmin):
    search_fields = ['user__email', 'production_api_key', 'developer_api_key']
    list_display = ['user']
