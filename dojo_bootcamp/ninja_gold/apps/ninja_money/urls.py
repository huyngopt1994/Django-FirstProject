from django.conf.urls import url
from . import views
urlpatterns = [
	url('^$', views.index ),
	url('^process_money$', views.process_money)
]