from django.shortcuts import render, redirect
from app.forms import *
from app.models import *
from accounts.models import *
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail


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
        'cat': cat,
    }

    return render(request, 'cat.html', context)


def toggle_bookmark(request, name):
    cat = Cat.objects.get(name=name)
    user = request.user
    active_user = User.objects.get(username=user.username)
    # bookmarked = False
    bookmark = Bookmark.objects.filter(user=active_user, cat=cat)
    all_bookmarks = Bookmark.objects.all()

    if bookmark.exists():
        bookmark.delete()
        bookmarked = False
    else:
        Bookmark.objects.create(user=request.user, cat=cat)
        bookmarked = True

    context = {
        'is_bookmarked': bookmarked,
        'all_bookmarks': all_bookmarks,
    }

    return render(request, 'partials/bookmark-button.html', context)


def send_message(request, name):
    cat = Cat.objects.get(name=name)
    user = request.user
    active_user = User.objects.get(username=user.username)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = active_user.email
            recipient_list = cat.user.email
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    fail_silently=False,
                )
            except Exception as e:
                print(e)
            return redirect('cat_details', name)
    else:
        form = MessageForm()

    return render(request, 'message-form.html', {'form': form})
