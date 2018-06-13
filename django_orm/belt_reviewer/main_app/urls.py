from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^$', views.index), #main page render form register and login, GET Method
    url(r'^books$', views.show_book), # page to show all books, GET method
	url(r'^books/add', views.add_book), #GET to render, POST to start to add
	url(r'^books/(?P<book_id>[1-9][0-9]*', views.show_book), # Get method
	url(r'^users/(?P<user_id>[1-9][0-9]*', views.show_user) #Get method
]
