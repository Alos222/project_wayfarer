from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name="about"),
    path('discover/', views.Discover.as_view(), name='discover'),
    path('user/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('view_post/<int:pk>/', views.ViewPost.as_view(), name='view_post'),
    path('view_post/<int:pk>/update/', views.UpdatePost.as_view(), name='post_update'),
    path('view_post/<int:pk>/delete/', views.DeletePost.as_view(), name="post_delete_confirmation"),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('user/<str:username>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('user/', views.LoginView.as_view(), name='login_redirect'),
]