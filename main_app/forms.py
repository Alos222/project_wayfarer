from enum import unique
from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.models import User
from .models import Post, Profile
from pyuploadcare.dj.forms import ImageField
from django.contrib.auth.forms import UserCreationForm

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'country', 'img']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'title', 'content', 'content_img']
        
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'content_img', 'location']
        
class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']