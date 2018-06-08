from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
	def validate(self,input_data):
		if not input_data['first_name'] or not input_data['last_name']:
			return False
		return True
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

	# overwrite models.Managers
	objects = UserManager()