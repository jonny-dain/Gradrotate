from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


from accounts.models import *

class AdminForm(ModelForm):

    PHASES = (
        ('Job creation','Job creation'),
        ('Intern collection','Intern collection'),
        ('Allocation','Allocation'),
    )

    phase = forms.ChoiceField(choices = PHASES , widget=forms.RadioSelect(attrs={'class' : 'btn-check', 'onchange': 'submit();'}))

    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['name','user']

       
    