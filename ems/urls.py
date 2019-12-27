"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from employee import views
from django.contrib.auth.views import *
from employee.views import (user_login, user_logout, user_register, success)
from django.urls import path,include

urlpatterns = [
    path('', include('employee.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('poll.urls')),
    path('employee/', include('employee.urls')),

    path('login/', views.user_login, name="user_login"),
    path('register/', views.user_register, name="user_register"),
    path('success/', views.success, name="user_success"),
    path('logout/', views.user_logout, name="user_logout"),
]
