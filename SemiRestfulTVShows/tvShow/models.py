from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['title'])<2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network'])<3:
            errors["network"] = "Network Should be at least 3 characters"
        if len(postData['description'])<10:
            errors["description"] = "Description Should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    objects = ShowManager()