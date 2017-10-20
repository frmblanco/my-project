from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, unique=True, )
    username = forms.CharField(max_length=30, blank=True)
    first_name = forms.CharField(max_length=45, blank=True)
    last_name = forms.CharField(max_length=45, blank=True)
    address = forms.CharField(max_length=200, blank=True)
    country = forms.CharField(max_length=200, blank=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','address', 'country')