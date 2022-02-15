from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from main_app.models import Post
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from main_app.forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile, Location, Post

from django.contrib.auth.models import User


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'
    
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


class ProfileView(TemplateView):
    template_name = 'profile.html'
<<<<<<< HEAD
=======
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = User.objects.get(username=context['username'])
        posts = Post.objects.filter(user=user)
        
        context['profile'] = user.profile
        context['user_posts'] = posts
        return context
      
>>>>>>> e9443f2f81ef233513318c7b95503d65f0ff49fa
class CreatePost(CreateView):
    model = Post
    fields = ['title', 'user', 'content', 'content_img', 'location']
    template_name = 'create_post.html'
    success_url = '/discover'
<<<<<<< HEAD
=======
    
>>>>>>> e9443f2f81ef233513318c7b95503d65f0ff49fa
class ViewPost(DetailView):
    model = Post
    template_name = 'view_post.html'
    
class UpdatePost(UpdateView):
    model = Post
template_name = 'post_update.html'   ##create post update page.
<<<<<<< HEAD
=======
    
>>>>>>> e9443f2f81ef233513318c7b95503d65f0ff49fa
    
class ProfileUpdate(UpdateView):
    
    def get(self, request, **kwargs):
        if request.user.is_authenticated and request.user.username == kwargs['username']:
            user_form = UserUpdateForm()
            profile_form = ProfileUpdateForm()
            context = {
                'user_form' : user_form,
                'profile_form' : profile_form
            }
            return render(request, 'profile_update.html', context)
        else:
            return redirect('/')
    
    def post(self, request, **kwargs):    
        if request.user.is_authenticated:
            if request.user.username != kwargs['username']:
                return redirect('profile', kwargs['username'])
            
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('profile', kwargs['username'])
            
        else:
            return redirect('/accounts/login')
        
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
        