from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    # path('', views.homefunction, name='home-page'),
    path('', PostListView.as_view(), name='home-page'),
    path('about/', views.aboutfunction, name='about-page'),
    path('userguide/', views.howToUse, name='userguide'),
    path('search_posts', csrf_exempt(views.search_posts), name='search_posts'),
    path('search/', views.searchfunction, name='search-page'),
    path('post/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),


]
