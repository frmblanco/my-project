from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def competitions_list(request):
    comps = Competitions.objects.select_related().order_by('-pub_date')
    return render(request, 'competitions/index.html', {'comps': comps})


def competitions_signup(request, pk):
    comps = get_object_or_404(Competitions, pk=pk)
    return render(request, 'competitions/signup.html', {"comps": comps})


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'competitions/registration.html', {'form': form})


def reg_success(request):
    return render(request, 'competitions/success.html', {})
