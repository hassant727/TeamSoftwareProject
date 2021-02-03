from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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