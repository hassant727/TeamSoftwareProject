from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from .models import Post, PostImage

from django.shortcuts import render
from django.views import View
from .forms import UserdataModelForm
from django.http import JsonResponse
from .price_predictor import predict





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

POST_FIELDS = [
        'title',
        'address_line_1',
        'address_line_2',
        'city',
        'county',
        'property_type',
        'number_of_bedrooms',
        'number_of_bathrooms',
        'property_description',
        'price',
        'energy_rating',
        'floor_plan',
        'size',
    ]

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = POST_FIELDS

    def form_valid(self, form):
        """ this function allows user to create a new post if they login """
        form.instance.author = self.request.user
        p = form.save()

        if self.request.POST:
            for file in self.request.FILES.getlist('post_images'):
                img = PostImage(post=p,image=file)
                img.save()

        f = UserdataModelForm(self.request.POST)
        print(f)

        data = f.cleaned_data

        no_rooms = data["number_of_bedrooms"]
        no_bathrooms = data["number_of_bathrooms"]
        size = data["size"]
        type = data["property_type"]
        energy_rating = data["energy_rating"]

        attributes = [[no_rooms, no_bathrooms, size, type, energy_rating]]
        print(predict(attributes))

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
                    img = PostImage(post=p,image=file)
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




