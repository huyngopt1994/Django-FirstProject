from django.shortcuts import render, reverse, redirect
from models import *
from django.contrib import  messages
# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request,'courses_app/index.html', {'courses': courses})

def create(request):
    if request.method == 'POST':
        input_data = request.POST
        if Course.objects.validate(input_data):

            Course.objects.create(name=input_data['name'],
                                  desc=input_data['desc'])
            messages.success(request, "You created sucessfully")
            return redirect(reverse('index'))
        else:
            messages.error(request, "You input is invalid, Please try")
            return redirect(reverse('index'))
def destroy_view(request, course_id):

    data = Course.objects.get(id=course_id)
    return render(request,'courses_app/destroy_view.html', {'data':data})

def confirm_destroy(request, course_id):
    try:
        Course.objects.get(id=course_id).delete()
    except Exception as e :
        messages.error(request,'Have some problems can"t delete')
        return redirect(reverse('index'))
    else:
        messages.success(request, 'We deleted course id %s' % course_id)
        return redirect(reverse('index'))