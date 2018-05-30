from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^surveys/process$', views.verify_submit),
	url(r'^result$' ,views.result)
]