from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField, UserChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label=""
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label=""
    )

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'}))

    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}