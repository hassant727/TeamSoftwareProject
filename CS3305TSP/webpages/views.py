from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
import json
from django.contrib.contenttypes import views
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.edit import ModelFormMixin
from django.db.models import Q

from .models import Post, PostImage

from django.shortcuts import render
from django.views import View
from .forms import UserdataModelForm
from django.http import JsonResponse
from .price_predictor import predict


def howToUse(request):
    return render(request, "webpages/user_guide.html")


def search_posts(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText', '')
        search_word = Post.objects.filter(
            title__istartswith=search_str) | Post.objects.filter(
            city__istartswith=search_str) | Post.objects.filter(
            property_description__icontains=search_str) | Post.objects.filter(
            address_line_1__icontains=search_str) | Post.objects.filter(
            address_line_2__icontains=search_str) | Post.objects.filter(
            county__icontains=search_str)
        data = search_word.values()
        return JsonResponse(list(data), safe=False)


def homefunction(request):
    """sql modeling passing in a dictionary of post """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'webpages/home.html', context)


def aboutfunction(request):
    return render(request, 'webpages/about.html', {'title': 'About'})


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


POST_FIELDS = [
    'address_line_1',
    'address_line_2',
    'city',
    'county',
    'property_type',
    'number_of_bedrooms',
    'number_of_bathrooms',
    'property_description',
    'price',
    'size',
    'energy_rating',
    'floor_plan',
]


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = POST_FIELDS

    def form_valid(self, form):
        """ this function allows user to create a new post if they login """
        form.instance.author = self.request.user
        self.object = form.save()
        if self.request.POST:
            for file in self.request.FILES.getlist('post_images'):
                img = PostImage(post=self.object, image=file)
                img.save()
            if form.is_valid():
                form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = POST_FIELDS

    def form_valid(self, form):
        """this function ensure that a user can only  update if they are login"""
        form.instance.author = self.request.user
        p = form.save()
        if self.request.POST:
            # remove relations of all old images of the post and attach new images
            # it also delete the file itself
            if self.request.FILES.getlist('post_images'):
                for images in p.post_images.all():
                    images.delete()
                for file in self.request.FILES.getlist('post_images'):
                    img = PostImage(post=p, image=file)
                    img.save()
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


class SearchResultView(ListView):
    model = Post
    template_name = "webpages/search.html"
    context_object_name = 'posts'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Post.objects.filter(Q(address_line_1__icontains=query) 
            | Q(address_line_2__icontains=query) 
                | Q(city__icontains=query )
                    | Q(county__icontains=query))