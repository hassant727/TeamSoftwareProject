from django.conf.urls import url
from django.urls import path
from . import views
from .views import LoginView, LogoutView


urlpatterns = [
    # authentication and login paths
    path('register/', views.register, name='register-page'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.activate,name='activate'),
    path('redirect/', views.redirectpages, name="redirect"),
    path('login', LoginView.as_view(), name="login"),
    path('profile/', views.profile, name='profile-page'),
    path('logout', LogoutView.as_view(), name="logout"),

    # the path to the chart
    path("chart/", views.line_chart, name="line_chart"),
    path("line_chart/json/", views.line_chart_json, name="line_chart_json"),
    path("line_highchart/json/", views.line_highchart_json, name="line_highchart_json"),


]