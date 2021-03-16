from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, SearchResultView
from . import views
"""
    urls path are define below
    name is used for template referencing
    the first entry in the function path is the url/that_name
    thos are imported from the views, which define are teh templates are rendered
"""
urlpatterns = [
    # path('', views.homefunction, name='home-page'),
    path('', PostListView.as_view(), name='home-page'),
    path('about/', views.aboutfunction, name='about-page'),
    path('userguide/', views.howToUse, name='userguide'),
    path('search_posts', csrf_exempt(views.search_posts), name='search_posts'),
    path('search/', SearchResultView.as_view(), name='search-page'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('dashboard', views.dashboardfunction, name="dashboard"),
    path('dashboard/function', views.dashboard_user_functionality, name="function"),
    path('dashboard/post', UserPostListView.as_view(), name='dashboard-post')


]
