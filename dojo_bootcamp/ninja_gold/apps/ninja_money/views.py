from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

# Create your views here.
def index(request):
	if 'total' not in request.session:
		request.session['total']= 0
	return render(request,"ninja_money/index.html")

def process_money(request,my_type):
	this_gold = 0
	action = 'earned'
	if my_type  == 'farm':
		this_gold = randint(10,21)
	elif my_type == 'cave':
		this_gold = randint(5,11)
	elif my_type == 'house':
		this_gold = randint(2,6)
	else:
		this_gold = randint(-50,51)
		if this_gold <0:
			action = 'lost'
	time_now =datetime.now().strftime("%Y/%m/%d %-I:%M%p")
	this_log = {
		'class': action,
		'message': "You {} {} golds from the {} ({})".format(action, abs(this_gold), my_type, time_now)
	}
	try:
		log_list = request.session['logs']
	except KeyError:
		log_list = []

	request.session['total'] += this_gold

	log_list.append(this_log)
	request.session['logs'] = log_list

	return redirect('/')