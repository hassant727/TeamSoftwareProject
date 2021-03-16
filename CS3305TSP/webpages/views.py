from django.contrib.auth.decorators import login_required
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
from django.db.models import Q, Avg

from .models import Post, PostImage

from django.shortcuts import render
from django.views import View
from .forms import UserdataModelForm
from django.http import JsonResponse
from .price_predictor import predict
from django.db.models import Sum
from django.shortcuts import render
from .price_predictor import predict_future_price
# from dashboard.views import dashboard_user_functionality, dashboardfunction
import os
import os.path


@login_required(login_url='/login/')
def dashboardfunction(request, **kwargs):
    """
        this function will display the average  selling price, estimated price and how much your properties worth
        this is displayed on the top in dashboard just below search menu

        month_price --> get the sum of estimated price of a specific user
        average_average --> average estimated price of a specific user posts
        assert_properties -->  sum of estimated prices

        if a user has no post return zeros else do the calculations and return the matrices and render it to the site
    """
    user = User.objects.get(username=request.user)
    post_count = float(Post.objects.count())
    print(post_count)
    value1 = {}
    value2 = {}
    value3 = {}
    value = {}

    month_price = Post.objects.filter(author=user).aggregate(total=Sum('estimated_price'))['total']
    average_average = Post.objects.filter(author=user).aggregate(total=Avg('estimated_price'))['total']
    assert_properties = Post.objects.filter(author=user).aggregate(total=Sum('estimated_price'))['total']
    print(month_price)

    if month_price is None:
        value1['monthly_estimate'] = 0
        value2['average_average'] = 0
        value3['assert_properties'] = 0
    else:

        value1 = {
            "monthly_estimate": round(month_price / post_count, 1)
        }
        value2 = {
            "average_average": average_average,
        }
        value3 = {
            "assert_properties": assert_properties
        }
        # os.remove("ChangedFile.csv")
        if os.path.isfile('estimate.json'):
            os.remove("estimate.json")
        print(os.path.isfile('estimate.json'))
        chart = {}
        chart['dict'] = json.dumps(predict_future_price(float(average_average)))
        # with open("json.txt", "w") as f:
        #     f.write(json.dumps(chart))

        with open("estimate.json", "w+") as file:
            json.dump(chart, file)
        print(chart)
        print(os.path.isfile('estimate.json'))
    value = {
        "value1": value1,
        "value2": value2,
        "value3": value3
    }
    #
    # if value1['monthly_estimate'] is None:
    #     value1['monthly_estimate'] = 0
    #     value2['average_average'] = 0
    #     value3['assert_properties'] = 0
    return render(request, 'dashboard/dashboard.html', value)


@login_required(login_url='/login/')
def dashboard_user_functionality(request):
    """
        render the specified template
    """
    return render(request, 'dashboard/all_user_function.html')


def howToUse(request):
    """
        render the specified template
    """
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
    """
        render the specified template
        context : sql modeling passing in a dictionary of post
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'webpages/home.html', context)


def aboutfunction(request):
    """
        render the specified template
    """
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
    """
        model: name of model, in this case post
        template_name: name of templates, in this case user_posts.html
        context_object_name: name of the object u want in the template in this case posts'
        paginate_by: how many post you want in each page, in this case 5

    """
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
    """
        post creation view, it requires the user to be login
        model type(as defined in the model file), in this case Post class
        fields: as define in the model, in this case POST_FIELDS
    """
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
    """
        same as above, the only difference is we delete the current images before updating new images
    """
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
    """
        delete view, delete  the post if the user that makes that request is the author
        this test_func() function ensures that only the user who posted it can edit it
         --> this use the UserPassesTestMixin

    """
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SearchResultView(ListView):
    """
        this view takes in parameter from teh search bar and searches it using
         addressline1, addressline2, city and county,
         returns all that matches, or none
    """
    model = Post
    template_name = "webpages/search.html"
    context_object_name = 'posts'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Post.objects.filter(Q(address_line_1__icontains=query)
                                   | Q(address_line_2__icontains=query)
                                   | Q(city__icontains=query)
                                   | Q(county__icontains=query))
