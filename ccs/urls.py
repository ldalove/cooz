from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ccs_list, name='ccs_list'),
	#url(r'^center/(?P<pk>\d+)/$', views.center_detail, name='center_detail'),
]
