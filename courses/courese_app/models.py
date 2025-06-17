from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['name'])<5:
            errors["name"] = "the name must be more the 5 char"
        if len(postData['description'])<15:
            errors["description"] = "the description must be more the 15 char"
        
        return errors



class Coureses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()