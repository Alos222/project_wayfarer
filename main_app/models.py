from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField 

class WayfarerUser(models.Model):
    # username, password, email, firstname, lastname already used by Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    img = ImageField(blank=True, manual_crop="")

class Location (models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    img = ImageField(blank=True, manual_crop="")
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(WayfarerUser, on_delete=models.CASCADE, related_name="posts")
    content = models.CharField(max_length=2000)
    content_img = ImageField(blank=True, manual_crop="")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

