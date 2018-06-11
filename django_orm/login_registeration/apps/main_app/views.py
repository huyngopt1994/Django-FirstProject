import bcrypt
from django.shortcuts import render, redirect
from models import *
from django.contrib import  messages

# Create your views here.
def index(request):
    return render(request,'main_app/index.html')

def success(request):
    # get user information depend on user_id
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'first_name':  user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }
    return render(request,'main_app/success.html', context)

def login(request):
    if request.method == 'POST':
        input_data = request.POST
        result = User.objects.validate_login(input_data)
        print (result)
        if not type(result) is list:
            user = User.objects.get(email=input_data['email'])
            request.session['user_id'] = user.id
            request.session['type'] = 'login'
            return redirect('/success')
        else:
            for error_message in result:
                messages.error(request, error_message)

    return redirect('/')

def register(request):
    if request.method == 'POST':
        input_data = request.POST
        print(input_data)
        errors = User.objects.validate_registration(input_data)
        if not (errors):
            hashed = bcrypt.hashpw(input_data['password'].encode(), bcrypt.gensalt(5))

            # ok the password so good ,  so we will create new row for new input data
            user = User.objects.create(first_name=input_data['first_name'],
                                last_name = input_data['last_name'],
                                email= input_data['email'],
                                password= hashed
                                )

            # should save user name  to session
            request.session['user_id'] = user.id
            request.session['type'] = 'register'
            return redirect('/success')
        else:
            for message_error in errors:
                messages.error(request, message_error)

    return redirect('/')
