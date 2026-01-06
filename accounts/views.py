from django.shortcuts import render, redirect
# from django.contrib import messages
from .forms import *
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserRegisterForm()
    
    return render(request, 'signup.html', {'form': form})


def admin_signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_superuser = True
            user.save()
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = LoginForm(request)

    return render(request, 'login.html', {'form': form})


def profile_view(request):
    return render(request, 'profile.html')