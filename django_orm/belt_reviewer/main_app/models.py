from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	poster = models.ForeignKey(User, related_name="uploaded_books")
	

# Create a middle table to handle many to many relationship

class Review(models.Model):
	content = models.TextField()
	user_review = models.ForeignKey('User', related_name="reviews")
	reviewed_book = models.ForeignKey('Book', related_name="reviews")
