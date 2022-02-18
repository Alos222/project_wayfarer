from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from main_app.forms import UpdatePostForm

from django.contrib.auth import login
from main_app.models import Post
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from main_app.forms import ProfileUpdateForm, CreatePostForm
from .models import Profile, Location, Post

from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
    def get(self, request, **kwargs):
        context = createAuthForms()
        return render(request, 'home.html', context)

class Discover(TemplateView):
    template_name = 'discover.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.request.GET.get('city')
        if city != None:
            context['locations'] = Location.objects.filter(name__icontains=city)
            context['post'] = Post.objects.filter(name__icontains=city)
        else: 
            context['locations'] = Location.objects.all()
            context['posts'] = Post.objects.all()
            
        context.update(createAuthForms())
        context['post_form'] = CreatePostForm()
        return context

class ProfileView(TemplateView):
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = User.objects.get(username=kwargs['username'])
        posts = Post.objects.filter(user=user)
        
        context['other_user'] = user
        context['user_posts'] = posts
        
        context.update(createAuthForms())
        return context 
    
class ProfileUpdate(UpdateView):
    
    def get(self, request, **kwargs):
        if request.user.is_authenticated and request.user.username == kwargs['username']:
            profile_form = ProfileUpdateForm()
            context = {
                'profile_form' : profile_form
            }
            context.update(createAuthForms())
            return render(request, 'profile_update.html', context)
        else:
            return redirect('/')
    
    def post(self, request, **kwargs):    
        if request.user.is_authenticated:
            if request.user.username != kwargs['username']:
                return redirect('profile', kwargs['username'])
            
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
            if profile_form.is_valid():
                profile_form.save()
                return redirect('profile', kwargs['username'])
            
        else:
            return redirect('/accounts/login')
        
class Signup(View):        
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/user/{}".format(user.username))
        
        else:
            context = {"signup_form": form}
            return render(request, 'home.html', context)
        
class CreatePost(CreateView):
    def post(self, request):
        post_form = CreatePostForm(request.POST)
        print(request.POST['user'])
        if post_form.is_valid():
            Post.objects.create(**post_form.cleaned_data)
            print(request.user.pk)
            # post.user = request.user.pk
            # post.save()
        return redirect('/discover')


class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'content', 'content_img', 'location']
    template_name = 'post_update.html'
    success_url = '/discover'##create post update page.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(createAuthForms())
        context['post_form'] = UpdatePostForm()
        return context

    def get_success_url(self):
        return reverse('view_post', kwargs={'pk': self.object.pk})


#########################
# class UpdatePost(UpdateView):
# 	def get(self, request, **kwargs):
# 		print(request.user.id)
# 		if request.user.is_authenticated and request.user.username == kwargs['username']:
# 			post_form = UpdatePostForm()
# 			context = {
# 				'post_form' : post_form
# 			}
# 			return render(request, 'post_update.html', context)
# 		else:
# 			return redirect('/')

# 	def post(self, request, **kwargs):    
# 		if request.user.is_authenticated:
# 			if request.user.username != kwargs['username']:  
# 				return redirect('profile', kwargs['username'])

# 			post_form = UpdatePostForm(request.POST, instance=request.user)
      
# 			if post_form.is_valid():
# 				post_form.save()
# 				return redirect('/discover', kwargs['username'])
# 		else:
# 			return redirect('/accounts/login')

# 	def get_success_url(self):
# 		return reverse('view_post', kwargs={'pk': self.object.pk})     
#####################

class ViewPost(DetailView):
    model = Post
    template_name = 'view_post.html'
    
class DeletePost(DeleteView):
    model = Post
    template_name = "post_delete_confirmation.html"
    success_url = "/discover"  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(createAuthForms())
        return context 
    
class LoginView(View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect("/user/{}".format(request.user.username))
        else:
            return redirect('/accounts/login/')
        
def createAuthForms():
    signup_form = UserCreationForm()
    login_form = AuthenticationForm()
    context = {
        'signup_form' : signup_form,
        'login_form' : login_form
    }
    return context
