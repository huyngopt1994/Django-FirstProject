from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index, name='index'), # GET method to display the index page
    url(r'^create$', views.create, name='create'), # POST method to create a new course
    url(r'^courses/(?P<course_id>[0-9]+)/destroy$', views.destroy_view,
    name='destroy_view'), # GET method to display delete page
    url(r'^courses/(?P<course_id>[0-9]+)/confirm', views.confirm_destroy,
    name='confirm_destroy') # GET  method to confirm that we will destroy this course_id
]