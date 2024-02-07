from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path("",views.accounts,name="accounts"),
    path("login",views.login,name="login")
]
