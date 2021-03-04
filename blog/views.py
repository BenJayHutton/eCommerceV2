from django.views.generic import ListView

from .models import Blog


class BlogListView(ListView):
    template_name = "blog/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context["title"] = "This is a blog"
        return context

    def get_queryset(self, *args, **kwargs):
        return Blog.objects.all()
