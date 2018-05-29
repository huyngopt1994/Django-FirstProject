from django.shortcuts import render
from time import gmtime, strftime
def index(request):
	date_time = strftime("%b %d, %Y - %H:%M %p", gmtime())
	date, time = date_time.split('-')
	context={
			'date': date,
			'time': time,
		}
	return render(request, 'display/index.html', context)

# Create your views here.
