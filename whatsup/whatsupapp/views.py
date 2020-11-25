from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def register(request):
    return render(request, 'register.html', {})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'profile.html', {'user': request.user})
