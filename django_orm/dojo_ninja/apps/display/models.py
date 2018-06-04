from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojos(models.Model):
	name =models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	desc = models.TextField(default="")

class Ninjas(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	dojo = models.ForeignKey(Dojos, related_name='ninjas')