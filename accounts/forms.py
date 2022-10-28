from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django import forms

class CreateUserForm(UserCreationForm):
    ROLE= [
    ('Intern','Intern/Graduate'), ('Manager','Manager')
    ]
    role_selection= forms.CharField(label='What role are you?', widget=forms.Select(choices=ROLE))

    class Meta:
        model = User
        fields = ['username','email','password1','password2','role_selection']

    