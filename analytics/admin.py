from django.contrib import admin

from .models import ObjectViewed, UserSession


@admin.register(ObjectViewed)
class ObjectViewedAdmin(admin.ModelAdmin):
    search_fields = ['user__email', 'ip_address']
    list_display = ['user', 'content_object', 'timestamp']


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    'user', 'ip_address', 'session_key', 'active', 'ended', 'timestamp'
