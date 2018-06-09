from __future__ import unicode_literals

from django.db import models

class CourseManger(models.Manager):
    def validate(self,data):
        if (len(data['name']) <5 or len(data['desc']) <15 ):
            return False
        return True

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    objects = CourseManger()
