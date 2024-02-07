from django.shortcuts import render, HttpResponse

# Create your views here.
def accounts(request):
    return HttpResponse("Hello World!")

def login(request):
    return render(request,"login.html")