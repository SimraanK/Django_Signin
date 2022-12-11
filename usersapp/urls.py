from django.contrib import admin
from django.urls import path, include
from usersapp import views


urlpatterns = [
    path("", views.usersApp, name="usersapp"),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    

]