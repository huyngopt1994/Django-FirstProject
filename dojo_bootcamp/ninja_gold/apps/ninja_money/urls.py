from django.conf.urls import url
from . import views
urlpatterns = [
	url('^$', views.index ),
	url('^process_money/(?P<my_type>\w+)$', views.process_money)
]