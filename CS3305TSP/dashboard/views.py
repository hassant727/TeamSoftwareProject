from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def dashboardfunction(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def dashboard_user_functionality(request):
    return render(request, 'dashboard/all_user_function.html')

