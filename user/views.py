from django.shortcuts import render, redirect
from django.contrib import auth
from custom_user.forms import CustomUserCreationForm


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user/success.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/registration.html', {'form': form})


def reg_success(request):
    return render(request, 'user/success.html', {})


def login(request):
    return render(request, 'user/login.html', {})


def logged(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return render(request, 'user/logged_in.html', {})

    else:
        return render(request, 'user/invalid_login.html', {})


def invalid_login(request):
    return render(request, 'user/invalid_login.html', {})


def logout(request):
    auth.logout(request)
    return render(request, 'user/logout.html', {})