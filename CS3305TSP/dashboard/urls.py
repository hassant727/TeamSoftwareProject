from django.urls import path
from . import views

urlpatterns = [
    # path('dashboard', views.dashboardfunction, name="dashboard"),
    # path('dashboard/function', views.dashboard_user_functionality, name="function"),
    path('delete_user', views.deleteUser, name='delete-user'),
    path('user_delete', views.confirmDeleteUser, name='confirm-delete-user')

]
