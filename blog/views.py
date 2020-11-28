from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Blog

class BlogListView(ListView):
    template_name = "blog/home.html"

    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context["title"]= "This is a blog"
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Blog.objects.all()
