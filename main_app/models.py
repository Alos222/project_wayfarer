from django.db import models
from pyuploadcare.dj.forms import ImageField 

# Create your models here.    
class Post(models.Model):
        
    title = models.CharField(max_length=200)
    user = models.CharField(max_length=300)
    content = models.CharField(max_length=2000)
    content_img = models.ImageField()
    content_imgtxt = models.CharField(max_length=500)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    
   