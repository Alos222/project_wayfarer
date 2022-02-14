from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile, Location, Post
from django.contrib.auth.models import User
# Authorization
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'
    
@method_decorator(login_required, name='dispatch')
class Discover(TemplateView):
    template_name = 'discover.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.request.GET.get('city')
        if city != None:
            context['locations'] = Location.objects.filter(name__icontains=city)
        else: 
            context['locations'] = Location.objects.all()
        return context

class Profile(TemplateView):
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = User.objects.get(username=context['username'])
        context['profile'] = user.profile
        return context
    
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
        