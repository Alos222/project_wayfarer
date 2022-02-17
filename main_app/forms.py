from django import forms
from django.contrib.auth.models import User
from .models import Post, Profile
from pyuploadcare.dj.forms import ImageField

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'country', 'img']
        
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'content_img', 'user', 'location']
        