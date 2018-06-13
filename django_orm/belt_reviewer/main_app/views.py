from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
	return render('main_app/index.html')

def register(request):
	if request.method == 'POST':

def login(request):
	if request.method == 'POST':

def logout(request):
	# please logout

def show_books(request):
	# This is method to show all books

def add_book(request):
	if request.method == 'GET':
		# This is GET method to render html file
	if request.method == 'POST':
		# This is POST method to add a new book

def show_book(request, book_id):
	"""This is method to render information of a book."""

def show_user(request, user_id):
	"""This is method to render information for a user."""