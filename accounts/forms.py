from django.forms import ModelForm, TextInput,EmailInput,PasswordInput, widgets
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django import forms
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm, SetPasswordForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'style': 'margin-bottom: 10px',
        'placeholder': 'Email',
        'type': 'email',
        'name': 'email'
        }))


class UserPasswordResetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'margin-bottom: 10px',
        'placeholder': 'New Password',
        'type': 'password',
        'name': 'password1'
        }))
    
    new_password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'margin-bottom: 10px',
        'placeholder': 'Repeat Password',
        'type': 'password',
        'name': 'password2'
        }))

    

    class Meta:
        fields = ('new_password1','new_password2')

    


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
    