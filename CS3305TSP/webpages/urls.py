from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    # path('', views.homefunction, name='home-page'),
    path('', PostListView.as_view(), name='home-page'),
    path('about/', views.aboutfunction, name='about-page'),
    path('search/', views.searchfunction, name='search-page'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

]
