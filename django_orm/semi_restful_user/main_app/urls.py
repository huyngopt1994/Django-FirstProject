from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^users$', views.list_all, name='list_all'), # Display alls (GET method)
    url(r'^users/new', views.new_user, name='new_user'), # Display edit page (GET method)
	url(r'^users/create', views.create_user, name='create_user'), # Create new user(POST method)
	url(r'^users/(?P<id_user>[0-9]+)$', views.handle_user, name='handle_user'), # List user infor page(GET method)
	url(r'^users/(?P<id_user>[0-9]+)/edit$', views.edit_view, name='edit_view'), # List user infor edit page(GET method)
	url(r'^users/(?P<id_user>[0-9]+)/update$', views.update_user, name='update_user'), # Update info for user(PUT method)
	url(r'^users/(?P<id_user>[0-9]+)/destroy$', views.destroy_user, name='destroy_user'), # Delete a user(GET Method)
]