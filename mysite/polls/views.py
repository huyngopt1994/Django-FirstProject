# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
#add more function for urls

def index(request):
    #query the last test polls
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)
def detail(request, question_id):
    return HttpResponse("You are looking at : %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting at : %s" % question_id)

# Create your views here.
