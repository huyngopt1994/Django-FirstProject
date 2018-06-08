from django.shortcuts import render, redirect
from django.urls import reverse # import this to use named route in views.pys
from django.contrib import messages
from models import *

# Create your views here.
def list_all(request):
	users = User.objects.all()
	return render(request, 'main_app/index.html', {'users': users})

def new_user(request):
	return render(request, 'main_app/new_user.html')

def create_user(request):
	if request.method == 'POST':
		if User.objects.validate(request.POST):
			User.objects.create(first_name = request.POST['first_name'],
			                    last_name=request.POST['last_name'],
			                    email= request.POST['email'])
			id_user = User.objects.get(first_name = request.POST['first_name'],
			                           last_name=request.POST['last_name'],
			                           email= request.POST['email']).id
			return redirect(reverse('handle_user', kwargs={'id_user': id_user}))

		else:
			messages.error(request,'Invalid information: your full name should larger than 5 characters')
			return redirect(reverse('new_user'))

def handle_user(request, id_user):
	"""Generate the page to show dashboard for one user"""
	user = User.objects.get(id=id_user)
	return render(request, 'main_app/user.html', {'user': user})

def edit_view(request,id_user):
	"""Generate the page to edit an user"""
	user = User.objects.get(id=id_user)

	return render(request, 'main_app/edit_user.html', {'user': user})

def update_user(request, id_user):
	"""Start to update information of specificed user"""
	print(request.method)
	if request.method == 'POST':
		if User.objects.validate(request.POST):
			print(request.POST)
			updated_user = User.objects.get(id = id_user)
			updated_user.first_name = request.POST['first_name']
			updated_user.last_name = request.POST['last_name']
			updated_user.email = request.POST['email']
			updated_user.save()
			return redirect(reverse('handle_user', kwargs={'id_user': id_user}))

def destroy_user(request, id_user):
	"""Delete a specificed user."""
	if request.method == 'GET':
		user = User.objects.get(id=id_user)
		user.delete()

	return redirect(reverse('list_all'))
