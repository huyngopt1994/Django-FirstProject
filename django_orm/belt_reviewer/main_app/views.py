from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

import bcrypt

# Create your views here.
def index(request):
	# just return the page
	return render(request,'main_app/index.html')

def register(request):
	if request.method == 'POST':
		post_data = request.POST
		result = User.objects.validate_register(post_data)
		if len(result) == 0 :
			# data is good
			User.objects.create(name = post_data['name'],
			                    alias = post_data['alias'],
			                    email = post_data['email'],
			                    password = bcrypt.hashpw(post_data['password'].encode(),bcrypt.gensalt(5)))
			messages.info(request,'Register succesfully, please sign in')
			return redirect('/')
		else:
			for my_error in result:
				messages.error(request,my_error)
			return redirect('/')

def login(request):
	if request.method == 'POST':
		post_data = request.POST
		result = User.objects.validate_login(post_data)
		if len(result) == 0 :
			# ok login should succesfully
			user = User.objects.get(email=post_data['email'])
			request.session['user_id'] = user.id
			# ok should redirect to main_page
			print(request.session['user_id'])
			return redirect('/books')

def logout(request):
	# yup we log out :
	# should reset
	request.session['user_id'] = None
	# we should redirect to login page
	return redirect('/')

def show_books(request):
	# This is method to show all books
	if request.session['user_id'] is None:
		messages.error('You should login if want to show informations')
		return redirect('/')
	else:
		# get detaied informations for books
		item={} #dictionary for item
		items =[]
		# query 3 lastest reviews (desencding
		all_reviews = Review.objects.all().order_by('-created_at')
		reviews = all_reviews[:3]
		for review in reviews:
			item['created_at'] = review.created_at
			item['rating'] = review.rating
			item['content'] = review.content
			item['user_name'] =review.reviewer.name
			item['title'] =review.book.title
			item['id'] = review.book.id
			items.append(item)
			item = {}
		print(items)
		books = set()
		# list all book which had reviews:
		for review in all_reviews:

			books.add((review.book.id, review.book.title))
		return render(request,'main_app/books.html',{'items':items,'books':books})

def add_book(request):
	if request.session['user_id'] is None:
		messages.error('You should login if want to show informations')
		return redirect('/')
	else:
		if request.method == 'GET':
			# This is GET method to render html file
			authors = Book.objects.all().values('author').distinct()
			print(authors)
			return render(request, 'main_app/add_book.html', {'authors': authors})
		if request.method == 'POST':
			post_data = request.POST
			if len(post_data['new_author']) >0:
				author = post_data['new_author']
			else:
				author = post_data['default_author']
			# This is POST method to add a new book
			# add new book
			user = User.objects.get(id=request.session['user_id'])
			book = Book.objects.create(title=post_data['title'],
			                           author= author,
			                           poster= user)

			# add review
			Review.objects.create(content= post_data['review'],
			                      rating=post_data['rating'],
			                      reviewer = user,
			                      book = book)

			return redirect('/books/%s' % book.id)


def show_book(request, book_id):
	"""This is method to render information of a book."""
	if request.session['user_id'] is None:
		messages.error(request, 'You should login if want to show informations')
		return redirect('/')
	else:
		book = Book.objects.get(id = book_id)
		print(book.author)
		all_reviews = book.reviews.all().order_by('-created_at')
		my_reviews = []
		my_review = {}
		reviews= all_reviews[:3]
		for review in reviews:
			my_review['rating'] = review.rating
			my_review['user_name'] = review.reviewer.name
			my_review['created_at'] = review.created_at
			my_review['user_id'] = review.reviewer.id
			my_reviews.append(my_review)
			my_review = {}

		return render(request, 'main_app/book.html', {'reviews': my_reviews,
		                                              'book':book})

def show_user(request, user_id):
	"""This is method to render information for a user."""
	if request.session['user_id'] is None:
		messages.error('You should login if want to show informations')
		return redirect('/')
	else:
		# show information of user
		user = User.objects.get(id=user_id)
		# get list of foreign key books
		# this will return a list of dictionary
		reviewed_books = user.reviews_left.all().values('book').distinct()
		books = [ Book.objects.get(id=item['book']) for item in reviewed_books ]
		total_reviews = len(books)
		return render(request, 'main_app/user.html',{'user':user,
		                                             'total_reviews': total_reviews,
		                                              'books':books})

def delete_review(request, review_id):
	pass

def create_review(request, book_id):
	pass
