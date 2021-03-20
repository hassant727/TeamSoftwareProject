from django.contrib import admin
from .models import Profile

"""
    registering the Profile section in the admin section
    this means gives you access to viewing all users from the admin portal
"""
admin.site.register(Profile)