from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate

from custom_user.forms import SignUpForm
from custom_user.models import CustomUserManager


def competitions_list(request):
    comps = Competitions.objects.select_related().order_by('-pub_date')
    return render(request, 'competitions/index.html', {'comps': comps})


def competitions_signup(request, pk):
    comps = get_object_or_404(Competitions, pk=pk)
    return render(request, 'competitions/signup.html', {"comps": comps})


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competitions/success.html')
    else:
        form = SignUpForm()

    return render(request, 'competitions/registration.html', {'form': form})


def reg_success(request):
    return render(request, 'competitions/success.html', {})


def login(self, request):
    if request.method == 'POST':
        form = self.form_class(request.POST)
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        login(request, user)
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('/')

    return render(request, 'competitions/login.html', {"form": form})