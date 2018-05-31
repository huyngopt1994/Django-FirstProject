from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'shop/index.html')

def checkout(request):
	return render(request,'shop/checkout.html')

def buy(request,number):
	pass