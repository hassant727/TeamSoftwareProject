from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


# @login_required
# def dashboardfunction(request):
#     return render(request, 'dashboard/dashboard.html')
#
# @login_required
# def dashboard_user_functionality(request):
#     return render(request, 'dashboard/all_user_function.html')

# @login_required
# def listing_total(request, **kwargs):
#     # user = get_object_or_404(User, username=kwargs.get('username'))
#     post = CS3305TSP.Post.objects.all()
#     total_invoice = post.aggregate(total=Sum('estimated_price'))['total']
#     # print(total_invoice)
#     return render(request, 'dashboard/dashboard.html', {'total_invoice': total_invoice})


def deleteUser(request):
    current_user = request.user
    username = current_user.username
    u = User.objects.get(username=username)
    u.delete()
    return render(request, 'userpages/register.html')



