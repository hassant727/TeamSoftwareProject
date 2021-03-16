from django.apps import AppConfig

"""
    this is created when you create a new app ( python manage.py startapp name_of_app)
    this represent an app your a main aplication
    remember that in django we can have multiple apps in an app
"""


class WebpagesConfig(AppConfig):
    name = 'webpages'
