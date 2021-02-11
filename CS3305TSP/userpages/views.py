# views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from random import randint, shuffle
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from chartjs.colors import COLORS, next_color
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
from .models import Meter


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login-page')
    else:
        form = UserRegisterForm()
    return render(request, 'userpages/register.html', {'form': form})


@login_required
def profile(request):
    """
    creating an instance of both userformUpdate and profileUpdateform
    then we storing in the current user details in u_form and p_form for profile picture within the first if condition
    this is so that the user can see the older credentials when they change to new,

    the 2nd if conditions saves the details if both forms are valid regardless of which form is chnaged

    :param request:
    :return: if updated we  redirect in place to avoid having to take to the last return which prompt users if they
    wish to reload th page which will submit the form again
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile-page')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {

        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'userpages/profile.html', context)


class ChartMixin(object):
    def get_providers(self):
        """Return names of datasets."""
        return ["year1", "year2", "year3"]

    def get_labels(self):
        """Return 12 labels."""
        return ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
                ]

    def get_data(self):
        """Return 3 random dataset to plot."""

        def data():
            """Return 12 randint between 0 and 100."""
            return [randint(0, 100) for x in range(12)]

        """change the number in range to increase line comparisons, you will have to increase the dataset as well """
        return [data() for x in range(1)]

    def get_colors(self):
        """Return a new shuffle list of color so we change the color
        each time."""
        colors = COLORS[:]
        shuffle(colors)
        return next_color(colors)


class LineChartJSONView(ChartMixin, BaseLineChartView):
    pass


class LineHighChartJSONView(ChartMixin, HighchartPlotLineChartView):
    title = _("Line HighChart Test")
    y_axis_title = _("Kangaroos")

    # special - line charts credits are personalized
    credits = {
        "enabled": True,
        "href": "http://example.com",
        "text": "Novapost Team",
    }


# Pre-configured views.
# colors = ColorsView.as_view()

line_chart = TemplateView.as_view(template_name="userpages/profile.html")
line_chart_json = LineChartJSONView.as_view()
line_highchart_json = LineHighChartJSONView.as_view()
