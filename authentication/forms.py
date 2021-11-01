from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
    UsernameField,
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

#"""-------------------------- SignUp Form --------------------------"""
class SignupForm(UserCreationForm):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        
# """-------------------------- Login Form --------------------------"""
class LoginForm(AuthenticationForm):
    username = UsernameField(
        required=True,
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autofocus": "current-password", "class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "password"]


# """-------------------------- ChangePassword Form --------------------------"""
class MyChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                "class": "form-control",
            }))
    new_password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}),
        help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}))

    class Meta:
        model = User
        fields = ["old_password", "new__password1", "new__password2"]

# """-------------------------- Create New User Form --------------------------"""
class AdminCreateUserForm(UserCreationForm):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name",
        required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name",
        required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email",
        required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

# """-------------------------- Update User Form --------------------------"""
class MyUserChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(label='First Name ',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class':'form-control',}))
    email=forms.EmailField(label='Email ID', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email']