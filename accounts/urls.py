from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.index,name="index"),

    # URL pattern for the registration view
    path('registration', views.registration_view, name='registration'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('loggedin', views.loggedin, name='loggedin'),
    
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password"),
    path('forget_message' , views.ForgetMessage, name="forget_message"),

]
