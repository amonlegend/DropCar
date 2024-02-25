from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.index,name="index"),

    # URL pattern for the registration view
    path('registration', views.registration_view, name='registration'),
    path('login', views.login_view, name='login'),
    path('loggedin', views.loggedin, name='loggedin'),
]
