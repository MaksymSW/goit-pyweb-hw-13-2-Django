from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, EmailField, EmailInput, PasswordInput

# from .models import Profile


class RegisterForm(UserCreationForm):
    username = CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control custom-border", 'placeholder': 'Enter your username'}))

    email = EmailField(max_length=100,
                               required=True,
                               widget=EmailInput(attrs={"class": "form-control custom-border", 'placeholder': 'name@example.com'}))

    password1 = CharField(max_length=50,
                                required=True,
                                widget=PasswordInput(attrs={"class": "form-control custom-border", 'placeholder': 'Enter your password'}))
    password2 = CharField(max_length=50,
                                required=True,
                                widget=PasswordInput(attrs={"class": "form-control custom-border", 'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = CharField(max_length=100,
                        required=True,
                        widget=TextInput(attrs={"class": "form-control custom-border", 'placeholder': 'Enter your username'}))
    
    password = CharField(max_length=20,
                        min_length=8, required=True,
                        widget=PasswordInput(attrs={"class": "form-control custom-border", 'placeholder': 'Enter your password'}))
    class Meta:
        model = User
        fields = ['username', 'password']


# class ProfileForm(forms.ModelForm):
#     avatar = forms.ImageField(widget=forms.FileInput())
#
#     class Meta:
#         model = Profile
#         fields = ['avatar']