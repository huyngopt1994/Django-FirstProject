from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'blog/index.html')

def new(request):
	return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
	#verify if request is POST or not
	if request.method == "POST":
		print ("*" * 50)
		print (request.POST)
		print (request.POST["name"])
		print (request.POST['desc'])
		#save  "test" into session with key is name
		request.session['name'] = request.POST["name"]
		if 'key' in request.session.keys():

			request.session['counter'] +=1
		else:
			request.session['counter'] =1
	return redirect('/blog')

def number_handler(request, number):
	return HttpResponse('placeholder to display blog %s' % number)

def edit(request, number):
	return HttpResponse('placeholder to edit blog %s' % number)

def delete(request, number):
	return redirect('/')