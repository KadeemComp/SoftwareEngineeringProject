"""Fruitdex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Home import views as home_views
from Users import views as user_views

urlpatterns = [
    path('', home_views.index , name = 'home_index'),
    path('admin/', admin.site.urls),
    path('Home/', include("Home.urls")),
    path('Users/', include("Users.urls")),
    path('browse', home_views.browse,name='browse' ),
    path('signup', user_views.signup_view, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'Users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Users/logout.html'), name = 'logout')
]
