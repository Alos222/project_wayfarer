from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from pyuploadcare.dj.forms import ImageField

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'country', 'img']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'title', 'content', 'content_img']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'title', 'content', 'content_img']

