from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request,'display/index.html')

def result(request):
	return render(request, 'display/result.html')

def verify_submit(request):
	if request.method =='POST':
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		if 'counter' in request.session:
			request.session['counter'] +=1
		else:
			request.session['counter'] = 1
		return  redirect('/result')
	return redirect('/')
