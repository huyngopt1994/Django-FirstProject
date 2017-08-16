# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
#add more function for urls

def index(request):
    #query the last test polls
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # add the lastest list into context
    context = {'latest_question_list': latest_question_list }

    return render(request,'polls/index.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def detail(request, question_id):
    try :
        # get object question from question_id
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exit")
    return render(request ,'polls/detail.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question,pk =question_id)
    print ("This is a a vote for : %s " % question.id)
    try:
        # get object choices ,request.POST['choice']=> return id of choice
        print request.POST
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except Choice.DoesNotExist:
        Choice.create(choice_text=question.question_text, votes=1)
        return HttpResponseRedirect(reverse('polls: results', args=(question.id,)))
    except KeyError:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "This is a key error",
        })
    else:
        # Increase the number of vote
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls: results', args=(question.id,)))

# Create your views here.
