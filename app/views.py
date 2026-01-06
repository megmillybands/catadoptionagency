from django.shortcuts import render, redirect
from app.forms import *
from app.models import *
from django.contrib.auth.models import User, Group


def home(request):
    cats = Cat.objects.all()
    context = {"cats": cats}
    return render(request, 'home.html', context)


def create_listing(request):
    # lister_group = Group.objects.get(name="Lister")
    # user = request.user
    if request.user.groups.filter(name="Lister").exists():
        if request.method == "POST":
            form = CatCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = CatCreationForm()
    else:
        return redirect('/')
    
    return render(request, 'cat-form.html', {'form': form})


# def get_listings(request):
#     cats = Cat.objects.all()
#     return render(request, "cat.html", {"cats": cats})
