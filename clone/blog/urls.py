from django.conf.urls import url
from blog import views
app_name="blog"
urlpatterns=[
  url(r'^about/$',views.about.as_view(),name='about'),
  url(r'^$',views.postlist.as_view(),name='postlist'),
  url(r'^post/(?P<pk>\d+)$',views.postdetail.as_view(),name="postdetail"),
  url(r'^post/new/$',views.postcreate.as_view(),name='postnew'),
  url(r'^post/(?P<pk>\d+)/edit/$',views.postupdate.as_view(),name='postedit'),
   url(r'^post/(?P<pk>\d+)/delete/$',views.postdelete.as_view(),name='postdelete'),
   url(r'^drafts/$',views.draftlist.as_view(),name='draftlist'),
   url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]
