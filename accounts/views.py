import os
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from DropCar import settings
from .models import CustomUser
import uuid
from .helpers import send_forget_password_mail
from .models import *
import requests
from inventory.models import Location
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.hashers import check_password

from django.core.files.storage import FileSystemStorage




# Create your views here.
def index(request):
    locations = Location.objects.all()
    locations_data = serialize('json', locations, fields=('location',))
    return render(request,"index.html", {"locations": locations_data,'user': request.user})

def loggedin(request):
    return render(request, "loggedin.html")

def my_Profile_view(request):
    return render(request, "myProfile.html")

def my_Booking_view(request):
    return render(request, "myBooking.html")

def terms_and_conditions_view(request):
    return render(request, 'terms.html')


# check if string is email
def is_email(string):
    if '@' in string:
        return True
    return False


def registration_view(request):
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # check if user exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            context = {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "password1": password1,
                "password2": password2,
            }
            return render(request, 'index.html', context=context)

        if password1 == password2:
            user = CustomUser(email=email, full_name=full_name, phone=phone)
            user.set_password(password1)
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('login')
    return render(request, 'UserLogin.html')


def login_view(request):
    user_is_authenticated = False
    button_text = "Login"
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if a user with the given email exists
        user_exists = CustomUser.objects.filter(email=email).exists()

        if not user_exists:
            messages.error(request, 'User does not exist')
            context = {
                "email": email,
                "password": password,
                "error": "User does not exist"
            }
            return render(request, 'UserLogin.html', context)

        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.error(request, 'Invalid Credentials')
            context = {
                "email": email,
                "password": password,
                "pwerror": "Invalid Credentials"
            }
            return render(request, 'UserLogin.html', context)
        elif user is not None and user.is_superuser:
            login(request, user)
            return redirect("/admin/")
        if user is not None and user.is_customer:
            login(request, user)
            user_info = {
                "is_authenticated": True,
                "email": user.email,
                "is_admin": user.is_admin,
                "is_customer": user.is_customer,
                "role": user.is_customer and "Customer" or user.is_admin and "Admin"
            }
            request.session['user_info'] = user_info
            messages.success(request, 'Login Successful')
            return redirect("/")
        
        else:
            if request.user.is_authenticated:
                user_is_authenticated = True
                button_text = "Profile"
              
    return render(request, 'UserLogin.html' , {"user_is_authenticated": user_is_authenticated, "button_text": button_text})


def logout_view(request):
    logout(request)
    return redirect('/')

def ChangePassword(request, token):
    try:
        profile_obj = Profile.objects.get(forget_password_token=token)
        user = profile_obj.user
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'change-password.html', {'token': token})
            user.set_password(new_password)
            user.save()
            
            # Clear forget password token
            profile_obj.forget_password_token = ''
            profile_obj.save()
            
            messages.success(request, 'Password changed successfully. Please login with your new password.')
            return redirect('login')
    except Profile.DoesNotExist:
        messages.error(request, 'Invalid token.')
        return redirect('/forget-password/')
    except Exception as e:
        messages.error(request, 'An error occurred.')
        print(e)
    
    return render(request, 'change-password.html', {'token': token})


def ForgetPassword(request):
        if request.method == 'POST':
            email = request.POST.get('email')
            
            if not CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'No user found with this email.')
                return redirect('/forget-password/')
            else:
                user_obj = CustomUser.objects.get(email=email)
                token = str(uuid.uuid4())
                profile_obj, created = Profile.objects.get_or_create(user=user_obj)
                profile_obj.forget_password_token = token
                profile_obj.save()
                send_forget_password_mail(user_obj.email, token)
                return redirect('forget_message')

        return render(request, 'forget-password.html')
    
def ForgetMessage(request):
    return render(request, 'forget-message.html')


# def update_profile(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         contact = request.POST.get('contact')
#         email = request.POST.get('email')

#         has_error = False

#         # Validate full name
#         if not full_name:
#             messages.error(request, 'Full name is required.', extra_tags='full_name')
#             has_error = True
#         elif len(full_name.split()) < 2:
#             messages.error(request, 'Please enter a full name with at least two words.', extra_tags='full_name')
#             has_error = True

#         # Validate contact
#         if not contact:
#             messages.error(request, 'Contact number is required.', extra_tags='contact')
#             has_error = True
#         elif not (contact.startswith('98') and len(contact) == 10):
#             messages.error(request, 'Contact number must be 10 digits long and start with 98.', extra_tags='contact')
#             has_error = True

#         # Validate email
#         if not email:
#             messages.error(request, 'Email is required.', extra_tags='email')
#             has_error = True
#         elif not email.endswith('@gmail.com'):
#             messages.error(request, 'Email must end with @gmail.com.', extra_tags='email')
#             has_error = True

#         if not has_error:
#             user = request.user
#             user.full_name = full_name
#             user.phone = contact
#             user.email = email
#             user.save()
#             messages.success(request, 'Your profile has been updated successfully')
#             return redirect('myProfile')

#     return render(request, "myProfile.html")

@login_required
def update_profile(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')

        has_error = False

        # Validate full name
        if not full_name:
            messages.error(request, 'Full name is required.', extra_tags='full_name')
            has_error = True
        elif len(full_name.split()) < 2:
            messages.error(request, 'Please enter a full name with at least two words.', extra_tags='full_name')
            has_error = True

        # Validate contact
        if not contact:
            messages.error(request, 'Contact number is required.', extra_tags='contact')
            has_error = True
        elif not (contact.startswith('98') and len(contact) == 10):
            messages.error(request, 'Contact number must be 10 digits long and start with 98.', extra_tags='contact')
            has_error = True

        # Validate email
        if not email:
            messages.error(request, 'Email is required.', extra_tags='email')
            has_error = True
        elif not email.endswith('@gmail.com'):
            messages.error(request, 'Email must end with @gmail.com.', extra_tags='email')
            has_error = True

        if not has_error:
            user = request.user
            user.full_name = full_name
            user.phone = contact
            user.email = email
            user.save()
            print("vayo")
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('myProfile')

    return render(request, "myProfile.html")



@login_required
def update_profile_pic(request):
    if request.method == 'POST':
        profile_pic = request.FILES['profile_pic']
        request.user.profile_pic = profile_pic
        request.user.save()
        messages.success(request, 'Your profile picture has been updated!')
        return redirect('myProfile')
    return render(request, 'myProfile.html')



@login_required
def update_password(request):
    error_messages = {
        'old_password_error': None,
        'new_password_error': None,
        'confirm_password_error': None
    }
    
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        user = request.user

        # Check if the old password matches the password in the database
        if check_password(old_password, user.password):
            # Check if the new passwords match
            if new_password1 == new_password2:
                # Update the user's password
                user.set_password(new_password1)
                user.save()
                messages.success(request, 'Your password was successfully updated!')
                return redirect('login')
            else:
                error_messages['confirm_password_error'] = 'New passwords do not match.'
        else:
            error_messages['old_password_error'] = 'Incorrect old password.'

    # Pass error_messages to the template context
    return render(request, 'myProfile.html', {'error_messages': error_messages})





