from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "User name", "class": "form-control bg-white border-left-0 border-md"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control bg-white border-left-0 border-md"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control bg-white border-left-0 border-md"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "confirm password", "class": "form-control bg-white border-left-0 border-md"}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]