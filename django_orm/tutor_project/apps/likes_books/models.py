from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	# Link for reference
	# https://docs.djangoproject.com/en/2.0/ref/models/fields/#emailfield
	email = models.EmailField(unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# Add one to many relationship
	uploader = models.ForeignKey(User, related_name='uploaded_books')
	# Add many to many relationship
	liked_users = models.ManyToManyField(User, related_name='liked_books')