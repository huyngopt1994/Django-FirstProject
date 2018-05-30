from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
	if 'counter' in request.session:
		request.session['counter'] +=1
	else:
		request.session['counter'] =1

	if 'string' not in request.session:
		request.session['string'] =''

	return render(request, 'display/index.html')

def generate(request):
	if request.method == "POST":
		unique_id = get_random_string(length=24)
		request.session['string'] = unique_id
	return redirect('/')
# Create your views here.
