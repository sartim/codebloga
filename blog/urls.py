from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^post/list', views.post_list, name='post-list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post-detail'),
    url(r'^post/new/$', views.post_new, name='post-create'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post-update'),


]
