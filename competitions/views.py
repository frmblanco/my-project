from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib import auth
from custom_user.forms import CustomUserCreationForm


def competitions_list(request):
    comps = Competitions.objects.select_related().order_by('-pub_date')
    return render(request, 'competitions/index.html', {'comps': comps})


def competitions_signup(request, pk):
    comps = get_object_or_404(Competitions, pk=pk)
    return render(request, 'competitions/signup.html', {"comps": comps})


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competitions/success.html')
    else:
        form = CustomUserCreationForm()

    return render(request, 'competitions/registration.html', {'form': form})


def reg_success(request):
    return render(request, 'competitions/success.html', {})


def login(request):
    return render(request, 'competitions/login.html', {})


def logged(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return render(request, 'competitions/logged_in.html', {})
    else:
        return render(request, 'competitions/invalid_login.html', {})


def invalid_login(request):
    return render(request,'competitions/invalid_login.html', {})