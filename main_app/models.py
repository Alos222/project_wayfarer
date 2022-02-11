from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField

# Create your models here.
class wfUser(models.Model):
    # username, password, email, firstname, lastname already used by Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = ImageField(blank=True, manual_crop="")