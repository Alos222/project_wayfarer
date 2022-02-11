from django.db import models

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=200)
    img = models.CharField()