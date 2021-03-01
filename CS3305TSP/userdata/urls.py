from django.urls import path
from django.views import View
from .views import UserdatFucntionView
urlpatterns = [
    path('userdata/', UserdatFucntionView.as_view(), name='userdata'),

]