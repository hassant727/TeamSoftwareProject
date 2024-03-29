"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# from . Users import views as user_views
# from users import views as user_views

urlpatterns = [
    # path('register/', views.register, name='register'),
    path('tsp13/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='userpages/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userpages/logout.html'), name='logout-page'),
    path('', include('userpages.urls')),
    path('', include('webpages.urls')),
    path('', include('dashboard.urls')),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='userpages/password_reset.html'),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(
        template_name='userpages/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='userpages/password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(
        template_name='userpages/password_reset_complete.html'),name='password_reset_complete'),

    path('chat/', include("chat.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


