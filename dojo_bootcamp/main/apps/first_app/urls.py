#sub url to despatch request to proper handler
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index) # add index function handlers for http://{{domain}}
]
