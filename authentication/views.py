from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request,"Invalid username or password!")
            return redirect('login')
        login(request,user)
        return redirect('home')
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # if not(first_name or last_name or username or password):
        #     messages.error(request, "All fields are required!")
        #     return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username alredy taken.')
            return redirect('register')
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password
        )
        user.save()
        messages.info(request,"Your account has been successfully created.")
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request,'dashboard.html')