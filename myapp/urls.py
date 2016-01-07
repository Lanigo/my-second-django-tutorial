from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^about/', views.about, name='about'),
	url(r'^blog/$', views.post_list, name='post_list'),
	url(r'^blog/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
	# add our url for comments here
	url(r'^blog/(?P<slug>[\w-]+)//comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]