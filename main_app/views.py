from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'
    
class Discover(TemplateView):
    template_name = 'discover.html'
    
class Profile(TemplateView):
    template_name = 'profile.html'
    
class Post(TemplateView):
    template_name = 'single_post.html'