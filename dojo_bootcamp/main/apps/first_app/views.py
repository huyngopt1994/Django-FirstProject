from django.shortcuts import render, HttpResponse, redirect # we have 3 ways : (render html, return HTTP response, redirect to some where)


# Create your views here.

def index(request):
	response = "Hello, I am the first request!"
	return HttpResponse(response)
