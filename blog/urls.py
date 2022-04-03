from django.urls import re_path


from .views import (
    BlogListView,
    BlogDetailSlugView,
    BlogCreateView,
    BlogUpdateView,
    blog_delete_view,
)

urlpatterns = [
    re_path(r'^$', BlogListView.as_view(), name='home'),
    re_path(r'^create/$', BlogCreateView.as_view(), name='create'),
    re_path(r'^update/(?P<slug>[\w-]+)/$', BlogUpdateView.as_view(), name='update'),
    re_path(r'^delete/(?P<slug>[\w-]+)/$', blog_delete_view, name='delete'),
    re_path(r'^view/(?P<slug>[\w-]+)/$', BlogDetailSlugView.as_view(), name='detail'),
]
