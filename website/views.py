#WEBSITE VIEWS

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

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