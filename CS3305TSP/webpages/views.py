from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from itertools import islice
from random import randint, shuffle

from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from chartjs.colors import COLORS, next_color
from chartjs.util import date_range, value_or_null
from chartjs.views.columns import BaseColumnsHighChartsView
from chartjs.views.lines import (
    BaseLineChartView,
    BaseLineOptionsChartView,
    HighchartPlotLineChartView,
)
from chartjs.views.pie import HighChartDonutView, HighChartPieView

# from CS3305TSP.models import Meter
# from TeamSoftwareProject.CS3305TSP.CS3305TSP.models import Meter

def homefunction(request):
    """sql modeling passing in a dictionary of post """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'webpages/home.html', context)


def aboutfunction(request):
    return render(request, 'webpages/about.html', {'title': 'About'})


def searchfunction(request):
    return render(request, 'webpages/search.html')


class PostListView(ListView):
    """
        this is a list view similar to the class above, --> does the same thing as the above but more efficient as it
        handles alot of forms work that you have to manual configure when uisng funtional views
        but passing different path names compare the convention formats--><appname>/<model>_<viewtype>.html
    """
    model = Post
    template_name = 'webpages/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'webpages/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """
            this function get the user if they exist else it returns 404 --> this function is used to filter and display
            a requested user
            filter by the user requested and sort by the latest post
        """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    """
        detail view, as as above but just using the generic django conventions
        <appname>/<model>_<viewtype>.html
        eg. how it looks
        blog/post_detail.html
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """ this function allows user to create a new post if they login """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """this function ensure that a user can only  update if they are login"""

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """this function ensures that only the user who post a comment can edit --> this use the UserPassesTestMixin """

        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'

    def test_func(self):
        """this function ensures that only the user who post a comment can edit --> this use the UserPassesTestMixin """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


