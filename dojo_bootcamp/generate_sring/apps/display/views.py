from django.shortcuts import render
from django.utils.crypto import get_random_string

def index(request):
	if 'counter' in request.session:
		request.session['counter'] +=1
	else:
		request.session['counter'] =1

	return render(request, 'display/index.html', context)

# Create your views here.
