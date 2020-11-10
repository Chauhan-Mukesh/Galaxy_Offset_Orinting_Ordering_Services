from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core import validators

from .models import User


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput({'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput({'placeholder': 'Last Name'}), required=True)
    email = forms.EmailField(widget=forms.TextInput({'placeholder': 'Email'}), required=True,
                             validators=[validators.validate_email])
    avatar = forms.FileField()
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'User Name', 'value': ' '}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Password'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Re-Enter Password'}), required=True)

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'avatar', 'email', 'password1', 'password2', 'gender']


class EditUserProfile(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput({'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput({'placeholder': 'Last Name'}), required=True)
    email = forms.EmailField(widget=forms.TextInput({'placeholder': 'Email'}), required=True,
                             validators=[validators.validate_email])
    avatar = forms.ImageField(required=False, validators=[validators.validate_image_file_extension])
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'User Name', 'value': ' '}), required=True)

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'avatar']
