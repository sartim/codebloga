from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^post/detail/(?P<pk>[0-9]+)/', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^post/create/$', views.PostCreate.as_view(), name='post-create'),
    url(r'post/update/(?P<pk>[0-9]+)/$', views.PostUpdate.as_view(), name='post-update'),
    # /app/country/delete/<country_id>/
    url(r'post/delete/(?P<pk>[0-9]+)/$', views.PostDelete.as_view(), name='post-delete'),


]
