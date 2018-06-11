# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.

class UserManager(models.Manager):
    def validate_login(self, input_data):
        errors = []
        # check DB if email existed or not
        if len(self.filter(email= input_data['email'])) >0 :
            # yep we got this user , so right now we will check this password
            user = self.get(email=input_data['email'])
            # verify the passed password and the stored password
            if not bcrypt.checkpw(input_data['password'].encode(), user.password.encode()):
                errors.append('password is incorrect')
        else:
            errors.append('email incorrect')

        if errors: # ok if we got an error
            return errors
        return user

    def validate_registration(self, input_data):
        errors = []

        # check the len of filed names :
        if len(input_data['first_name']) < 2 or len(input_data['last_name']) <2 :
            errors.append('name fields must be at least 3 characters')
        # check len of password :
        if len(input_data['password']) <8 :
            errors.append('password must be at least 8 characters')

        # verify first name and last name should contain only alpha character
        if not re.match(NAME_REGEX,input_data['first_name']) or not re.match(NAME_REGEX, input_data['last_name']):
            errors.append('your name should contain only alpha characters')

        # verify email is invalid or not
        if not re.match(EMAIL_REGEX, input_data['email']):
            errors.append('email is invalid')

        # verify confirm_password and password
        if input_data['confirm_password'] != input_data['password']:
            errors.append('confirm_password doesn"t match with password')

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()
    def __str__(self):
        return self.email