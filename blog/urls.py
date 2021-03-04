from django.conf.urls import url


from .views import (
    BlogListView,
    BlogDetailSlugView,
    BlogCreateView,
    BlogUpdateView,
    blog_delete_view,
)

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='home'),
    url(r'^create/$', BlogCreateView.as_view(), name='create'),
    url(r'^update/(?P<slug>[\w-]+)/$', BlogUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<slug>[\w-]+)/$', blog_delete_view, name='delete'),
    url(r'^view/(?P<slug>[\w-]+)/$', BlogDetailSlugView.as_view(), name='detail'),
]
