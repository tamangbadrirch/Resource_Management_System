"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from user_mgmt.views import UserLoginView, UserAddView
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', UserLoginView.as_view(), name="login"),
    path('signup',UserAddView.as_view(),name="UserSignUp"),
    path('user/add',UserAddView.as_view(),name="Useradd"),
    path('home', views.INDEX, name='home'),  #views.py ma INDEX vanne function xa vaneko
    path('add', views.ADD, name='add'),
    path('edit', views.EDIT, name='edit'),
    path('', views.LANDING, name='landing'),
    path('search', views.SEARCH, name='search'),
    path('logout', views.LOGOUT, name='logout'),
    path('update/<str:id>', views.UPDATE, name='update'),
    path('delete/<str:id>', views.DELETE, name='delete'),
]
