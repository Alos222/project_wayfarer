from django.contrib import admin

from main_app.models import WayfarerUser, Post, Location

# Register your models here.
admin.site.register(WayfarerUser)
admin.site.register(Post)
admin.site.register(Location)
