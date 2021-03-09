from django.shortcuts import render


# Create your views here.

def dashboardfunction(request):
    return render(request, 'dashboard/dashboard.html')

