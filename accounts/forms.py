from django.forms import ModelForm, TextInput,EmailInput,PasswordInput, widgets
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django import forms

class CreateUserForm(UserCreationForm):
    ROLE= [
    ('Intern','Intern/Graduate'), ('Manager','Manager')
    ]
    role_selection= forms.CharField(label='What role are you?', widget=forms.Select(choices=ROLE))
    role_selection.widget.attrs.update({'class': 'form-select'})
# choicefiled

    class Meta:
        model = User
        fields = ['username','email','password1','password2','role_selection']

        
        
        
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'style': 'margin-bottom: 10px'
            })
        self.fields['email'].widget = widgets.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                'style': 'margin-bottom: 10px'
            })
        self.fields['password1'].widget = widgets.PasswordInput(
            attrs={
                'placeholder': 'New password',
                'class': 'form-control',
                'style': 'margin-bottom: 10px'
            })
        self.fields['password2'].widget = widgets.PasswordInput(
            attrs={
                'placeholder': 'Repeat password',
                'class': 'form-control',
                'style': 'margin-bottom: 10px'
            }) 
        #self.fields['role_selection'].widget = widgets.Select(
        #    attrs={
        
        #        'class': 'bootstrap-select'
                
        #    }) 
    