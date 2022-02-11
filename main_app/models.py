from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    img = ImageField(blank=True, manual_crop="")
    POI = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="point of interest")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
