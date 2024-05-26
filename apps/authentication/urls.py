# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, edit_user
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('adduser', views.get_users, name="adduser" ),
    path('createuser', views.create_user, name="create_user" ),
    path('edituser', edit_user, name='edit_user'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('update_user', views.update_user, name='update_user'),
]
