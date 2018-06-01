from django.shortcuts import render, redirect

#build dictionary to store a products
PRODUCT = [
	{'name':'Dojo Tshirt',
	 'price': 19.99,
	 'id': 1,
	 },
    {'name':'Dojo Sweater',
	 'price': 29.99,
	 'id': 2,
	 },
    {'name':'Dojo Cup',
	 'price': 4.99,
	 'id': 3,
	 },
    {'name':'Algorithm Book',
	 'price': 40.99,
	 'id': 4,
	 }
]
# Create your views here.
def index(request):
	context= {
		'items':PRODUCT
	}
	return render(request,'shop/index.html',context)

def checkout(request):

	return render(request,'shop/checkout.html')

def buy(request,id):
	print(id)
	if request.method == 'POST':
		for item in PRODUCT:
			print(item['id'])
			if item['id'] == int(id):
				print('say oh yeah')
				price = item['price']
				break
		else:
			return redirect('/amadon')
		quantity = int(request.POST['quantity'])
		request.session['money'] = quantity * price
		request.session['price'] = price
		if 'total_money' not in request.session:
			request.session['total_money'] = 0
		if 'total_quantity' not in request.session:
			request.session['total_quantity'] = 0
		request.session['total_money'] += request.session['money']
		request.session['quantity'] = quantity
		request.session['total_quantity'] += quantity
		return redirect('/amadon/checkout')
	return redirect('/amadon')


def clear(request):
	for key in list(request.session.keys()):
		del request.session[key]
	return redirect('/amadon')