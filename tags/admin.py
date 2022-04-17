from django.contrib import admin

from .models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name', 'blurb']
    list_display = ['name', 'public']
