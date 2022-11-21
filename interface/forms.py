from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


from accounts.models import *

class AdminForm(ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['name','user']
