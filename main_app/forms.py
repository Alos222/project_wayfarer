from django import forms
from django.contrib.auth.models import User
from .models import Post, Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'country', 'img']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'title', 'content', 'content_img', 'user']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'title', 'content', 'content_img', 'user']

