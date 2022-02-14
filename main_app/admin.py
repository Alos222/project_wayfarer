from django.contrib import admin

from main_app.models import Profile, Post, Location

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'country')

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post)
admin.site.register(Location)
