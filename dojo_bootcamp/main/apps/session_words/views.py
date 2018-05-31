# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "session_words/index.html")

def add_word(request):
    new_word = {}
    # loop
    for key, value in request.POST.items():
        if key != "csrfmiddlewaretoken" and key != "show_big":
            new_word[key] = value
        if key == "show_big":
            new_word['big'] = "big"
        else:
            new_word['big'] = ""
    # add created_at into new words
    new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    if 'data' not in request.session:
        request.session['data'] = []

    # add this new_word to session data
    temp_list = request.session['data']
    temp_list.append(new_word)

    request.session['data'] = temp_list
    for key, val in request.session.items():
        print (key, val)
    print ("past craeted at", new_word)

    return redirect('/session_words')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/session_words')