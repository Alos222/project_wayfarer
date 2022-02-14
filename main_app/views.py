from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'
    
class Discover(TemplateView):
    template_name = 'discover.html'
    
class Profile(TemplateView):
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = User.objects.get(username=context['username'])
        context['profile'] = user.profile
        return context
    
# class ProfileUpdate(UpdateView):
#     template_name = 'profile_update.html'
#     model = Profile
#     fields = ['city', 'country', 'img']
#     success_url = "/"
    
    
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
        