from django import forms
from django.contrib.auth.models import User
from gamestrike_app import models

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "login-input", "placeholder": "First Name"}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "login-input", "placeholder": "Last Name"}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class": "login-input", "placeholder": "Email"}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "login-input", "placeholder": "Username"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class": "login-input", "placeholder": "Password"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class UserProfileForm(forms.ModelForm):
    description = forms.CharField(required=False, max_length=350, label="", widget=forms.Textarea(attrs={"class": "login-input", "placeholder": "Description"}))
    profile_picture = forms.ImageField(required=False, label="Profile Picture", widget=forms.FileInput(attrs={"class": "file-input"}))

    class Meta:
        model = models.UserProfile
        fields = ('description', 'profile_picture')

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "login-input", "placeholder": "First Name"}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "login-input", "placeholder": "Last Name"}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class": "login-input", "placeholder": "Email"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
