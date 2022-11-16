from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django import forms

from accounts.models import *

class StudentForm(ModelForm):
    class Meta:
        model = Intern
        fields = '__all__'
        exclude = ['user','progress','coding','project_management','marketing_skills','web_skills','first_preference', 'second_preference', 'third_preference']

class ManagerForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['user','coding','project_management','marketing_skills','web_skills']


