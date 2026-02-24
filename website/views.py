#WEBSITE VIEWS

from django.shortcuts import render
from django.contrib import messages

def home(request):
    return render(request,'website/home.html')

def about_us(request):
    return render(request,'website/about_us.html')

def contact_us(request):
    return render(request,'website/about_us.html')

def tos(request):
    return render(request,'website/tos.html')

def privacy(request):
    return render(request,'website/privacy.html')

def signup(request):
    return render(request,'website/signup.html')

def login(request):
    messages.success(request,"success test")
    return render(request,'website/login.html')