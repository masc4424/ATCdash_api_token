"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ATCdash import views
from django.contrib.auth import views as auth_views

from ATCdash.views import UserList, UserDetail

from ATCdash.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls, name='djangoadmin'),
    path('', views.home, name='login'),
    path('main/', views.dashboard, name='dashboard'),
    path('logout/', views.log_out, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('profile_image/', views.generate_profile_image, name='generate_profile_image'),

    # Reset Password #
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    # api
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]