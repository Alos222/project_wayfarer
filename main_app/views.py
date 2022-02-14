from turtle import title
from django.shortcuts import render
from pydantic import PostgresDsn
from .models import Post as PostModel
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'
    
class Discover(TemplateView):
    template_name = 'discover.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context["posts"] = PostModel.objects.filter(name__icontains=title)
        else:
            context["posts"] = PostModel.objects.all()
        return context
    
class Profile(TemplateView):
    template_name = 'profile.html'
    
class Post(TemplateView):
    template_name = 'single_post.html'