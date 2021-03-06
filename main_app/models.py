from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField 
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    # username, password, email, firstname, lastname already used by Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    img = ImageField(blank=True, manual_crop="")
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
        
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

class Location (models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="")
    img = ImageField(blank=True, manual_crop="")
    
    def __str__(self):
        return "{}, {}".format(self.city, self.country)
    
class Post(models.Model):
    title = models.CharField(blank=False, max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.CharField(blank=False, max_length=2000)
    content_img = ImageField(blank=True, manual_crop="")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="posts")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    