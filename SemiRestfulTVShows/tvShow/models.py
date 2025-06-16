from django.db import models

# Create your models here.

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField()