from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.CharField(auto_now_add=True)

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	poster = models.ForeignKey(User, related_name="uploaded_books")
	

