from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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
    
class Signup(View):
    def get(self, request):
        signup_form = UserCreationForm()
        context = {"form" : signup_form}
        return render(request, "registration/signup.html", context)
        
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/user/{}".format(user.username))
        
        else:
            context = {"signup_form": form}
            return render(request, 'registration/signup.html', context)
        