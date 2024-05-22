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
    path('myProfile', views.my_Profile_view, name='myProfile'),
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password"),
    path('forget_message' , views.ForgetMessage, name="forget_message"),
    path('update_profile', views.update_profile, name='update_profile'),
    path('update_profile_pic', views.update_profile_pic, name='update_profile_pic'),
    path('update_password', views.update_password, name='update_password'),
    path('my_booking', views.my_Booking_view, name='my_booking'),
    path('terms-and-conditions/', views.terms_and_conditions_view, name='terms_and_conditions'),
]
