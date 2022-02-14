from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('discover/', views.Discover.as_view(), name='discover'),
    path('user/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('user/<str:username>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
]