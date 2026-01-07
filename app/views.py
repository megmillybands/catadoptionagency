from django.shortcuts import render, redirect
from app.forms import *
from app.models import *
from django.contrib.auth.models import User, Group


def home(request):
    cats = Cat.objects.all()
    context = {"cats": cats}

    return render(request, 'home.html', context)


def create_listing(request):
    user = request.user
    active_user = User.objects.get(username=user.username)
    if active_user.groups.filter(name="Lister").exists():
        if request.method == "POST":
            form = CatCreationForm(request.POST, request.FILES, user=active_user)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = CatCreationForm(user=active_user)
    else:
        return redirect('/')
    
    return render(request, 'cat-form.html', {'form': form})


def cat_details(request, name):
    cat = Cat.objects.get(name=name)
    context = {
        'cat': cat
    }
    return render(request, 'cat.html', context)