from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):

    First_name = forms.CharField(max_length=100, help_text='Last Name')
    Last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ['username', 'First_name', 'Last_name', 'email', 'password1', 'password2']