from django.contrib import admin

from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ['user__email', 'title', 'blog_post', 'tags__name']
    list_display = ['user', 'title', 'date']

    'user', 'title', 'slug', 'date', 'blog_post', 'tags'
