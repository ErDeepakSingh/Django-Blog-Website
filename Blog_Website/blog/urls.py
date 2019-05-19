from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.PostListView.as_view(),name='Blog_home'),
    url(r'^new/$', views.PostCreateView.as_view(), name='Blog_create'),
    url(r'^(?P<username>\w+)',views.UserPostListView.as_view(),name='user_posts'),
    url(r'^update/$',views.PostUpdateView.as_view(),name='Blog_update'),
    url(r'^about/$', views.Blog_about, name='Blog_about'),
    url(r'^(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='blog_details'),
    url(r'^(?P<pk>\d+)/update/$',views.PostUpdateView.as_view(),name='blog_update'),
    url(r'^(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='blog_delete'),
    # url(r'^blog/$',views.Blog_home,name='blog_home')
]
# r'^(?P<post_id>\d+)/$
# r'^blog/(?P<blog_id>\d+)/