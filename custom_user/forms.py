from django import forms
from django.contrib.auth.forms import UserCreationForm
from custom_user.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=45, required=True)
    last_name = forms.CharField(max_length=45, required=True)
    country = forms.CharField(max_length=30, required=True)
    postal = forms.CharField(max_length=5, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'country', 'postal',)
