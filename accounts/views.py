from django.shortcuts import render, redirect
from .forms import *
from accounts.models import *
from app.models import *
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            selected_groups = form.cleaned_data['user_type']
            for group in selected_groups:
                user.groups.add(group)
            user.save()
            return redirect('/')
    else:
        form = UserRegisterForm()
    
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm(request)

    return render(request, 'login.html', {'form': form})


def profile_view(request):
    user = request.user
    active_user = User.objects.get(username=user.username)
    user_cats = Cat.objects.filter(user=active_user)
    context = {"cats": user_cats}

    return render(request, 'profile.html', context)


# def edit_account(request):
