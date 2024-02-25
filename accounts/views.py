from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.
def index(request):
    return render(request,"index.html")

def loggedin(request):
    return render(request, "loggedin.html")

# check if string is email
def is_email(string):
    if '@' in string:
        return True
    return False


def registration_view(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        full_name = request.POST.get("full_name")
        # last_name = request.POST.get("last_name")
        email = request.POST.get('email')
        # dob = request.POST.get('dob')
        # address = request.POST.get('address')
        phone = request.POST.get('phone')
        # gender = request.POST.get('gender')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # check if user exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            context = {
                # "username": username,
                "full_name": full_name,
                # "last_name": last_name,
                "email": email,
                # "dob": dob,
                # "address": address,
                "phone": phone,
                # "gender": gender,
                "password1": password1,
                "password2": password2,
                # "username_error": "User already exists"
            }
            return render(request, 'index.html', context=context)

        if password1 == password2:
            user = User(email=email, full_name=full_name, phone=phone)
            user.set_password(password1)
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('/')
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if is_email(email):
            username = User.objects.get(email=email).username
            user_exists = User.objects.filter(email=email).exists()
        else:
            user_exists = User.objects.filter(
                username=email).exists()
            username = email

        if not user_exists:
            messages.error(request, 'User does not exist')
            context = {
                "email": email,
                "password": password,
                "error": "User does not exist"
            }
            return render(request, 'login.html', context)

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Credentials')
            context = {
                "email": email,
                "password": password,
                "pwerror": "Invalid Credentials"
            }
            return render(request, 'login.html', context)
        elif user is not None and user.is_superuser and user.is_staff:
            login(request, user)
            return redirect("/admin")
        if user is not None and user.is_customer or user.is_farmer:
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
            return redirect("loggedin")
        

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')
