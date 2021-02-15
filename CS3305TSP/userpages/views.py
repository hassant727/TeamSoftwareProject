# views here.
import json
from random import randint, shuffle
from chartjs.colors import COLORS, next_color
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.views.generic import TemplateView
from validate_email import validate_email

from .forms import UserUpdateForm, ProfileUpdateForm
from .utils import account_activation_token

"""-----------------This section deals with authentication---------------"""


class RegistrationView(View):
    def get(self, request):
        return render(request, 'userpages/register.html')

    def post(self, request):
        # GET USER DATA
        # VALIDATE
        # create a user account

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'userpages/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_body = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }

                link = reverse('activate', kwargs={
                    'uidb64': email_body['uid'], 'token': email_body['token']})

                email_subject = 'Activate your account'

                activate_url = 'http://'+current_site.domain+link

                email = EmailMessage(
                    email_subject,
                    'Hi '+user.username + ', Please the link below to activate your account \n'+activate_url,
                    'noreply@semycolon.com',
                    [email],
                    )
                email.send(fail_silently=False)
                messages.success(request, f"An Account activation link has ben sent to {user.email}")
                return redirect('login')

        return render(request, 'userpages/register.html')


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use,choose another one '}, status=409)
        return JsonResponse({'email_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use,choose another one '}, status=409)
        return JsonResponse({'username_valid': True})


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login' + '?message=' + 'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')


def activate(request, uidb64, token):
    """
    :param request: self explainatory
    :param uidb64: json encoding base 64 format
    :param token: reset token being created using the passwordreset token generator to ensure unique password token
                  is generated everytime
    :return: redirect the pages to login once the user clicks on their link to send an email or throws in an error
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('userpages/activated_account.html')
        HttpResponse('Thank you for your email confirmation. you will be redirected in 2 seconds')
        return redirect('redirect')

        # return redirect('userpages/login.html')
    else:
        return HttpResponse('Activation link is invalid!')


def activated(request):
    return render(request, 'userpages/activated_account.html')


def redirectpages(request):
    """this will be used to redirect all 404 errors to this page"""
    return render(request, "userpages/redirect.html")


class LoginView(View):
    def get(self, request):
        return render(request, 'userpages/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username + ' you are now logged in')
                    return redirect('profile-page')
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'userpages/login.html')
            messages.error(
                request, 'Invalid credentials,try again')
            return render(request, 'userpages/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'userpages/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')


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


"""-----------The section below is for chart/graph manipulation--------"""


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
