from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField, UserChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'}
            ),
        label=""
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'}
            ),
        label=""
    )

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Username')}
            ),
        help_text="",
        )

    first_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('First name')}
            ),
        help_text="",
        )

    last_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Last name')}
            ),
        help_text="",
        )

    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Email')}
            ),
        )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password')}
            )
        )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password confirmation')}
            )
        )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        field_classes = {'username': UsernameField}

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Email')}
            ),
        )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('New password')}
            )
        )

    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('New password confirmation')}
            )
        )