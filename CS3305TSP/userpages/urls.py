from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('profile/', views.profile, name='profile-page'),

    # the path to the chart
    path("chart/", views.line_chart, name="line_chart"),
    path("line_chart/json/", views.line_chart_json, name="line_chart_json"),
    path("line_highchart/json/", views.line_highchart_json, name="line_highchart_json"),
]