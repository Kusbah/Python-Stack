from django.db import models
import re
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if Users.objects.filter(email=postData['email']).exists():
            errors["email"] = "Email already exists!"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address!"
        if len(postData['first_name'])<2:
            errors["first_name"] = "First Name should be more then 2 char"
        if len(postData['last_name'])<2:
            errors["last_name"] = "Last Name should be more then 2 char"
        if len(postData['password'])<8:
            errors["password"] = "password should be more then 8 char"
        if postData['password'] != postData['confirm_password']:
            errors["password"] = "Passwords do not match"
        return errors



class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField()
    objects = UserManager()