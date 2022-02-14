from django.contrib import admin

from main_app.models import Profile, Post, Location

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Location)
