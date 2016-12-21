from django.conf.urls import url

from . import views

urlpatterns = [
	# match every request(^$) into index view
	url(r'^$', views.index, name='index'),
	url(r'^(?P<chorelist_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<chorelist_id>[0-9]+)/chores/(?P<chore_id>[0-9]+)/$', views.choredetail, name='choredetail')
]