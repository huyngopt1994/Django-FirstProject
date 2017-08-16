"""Create a url conf"""

from django.conf.urls import url, include
from django.contrib import admin
from . import views

# wire some url to view
urlpatterns = [
    #ex: /polls/
    url(r'^$', views.index, name ='index'),
    #ex /polls/5
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #ex pollls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
    #ex polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote')
]
