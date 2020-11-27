from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'index.html', {})

def register(request):
    return render(request, 'register.html', {})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'profile.html', {'user': request.user})

def everyone(request):
    # https://stackoverflow.com/a/23139674
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'everyone.html', {'users_list': users})
