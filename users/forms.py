from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django import forms

from accounts.models import *

class StudentForm(ModelForm):

    #REMOTE_CHOICES = [
    #    ('Everyday', 'Everyday'),
    #    ('3-4', '3-4'),
    #    ('1-2','1-2'),
    #    ('Remote','Remote'),
    #]
    #remote_choice = forms.CharField(label='What role are you?', widget=forms.Select(choices=REMOTE_CHOICES))
    #remote_choice.widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Intern
        fields = '__all__'
        exclude = ['user','email','progress','location','remote','coding','project_management','marketing_skills','web_skills','first_preference', 'second_preference', 'third_preference']
    
        


    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget = widgets.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': 'form-control',
                'style': 'margin-bottom: 10px'
            })

class StudentForm2(ModelForm):

    LOCATIONS=[('Newbury','Newbury'),
        ('London Paddington', 'London Paddington'),
        ('Speechmark','Speechmark')]


    pref_location = forms.ChoiceField(choices=LOCATIONS, widget=forms.RadioSelect(
            attrs={'class': 'inline'}
        ))


    REMOTE_OPTIONS= [
        ('Everyday', 'Everyday'),
        ('3-4', '3-4'),
        ('1-2','1-2'),
        ('Remote','Remote')
    ]
    remote_option= forms.CharField(label='Preferred number of days in the office *', widget=forms.Select(choices=REMOTE_OPTIONS))
    remote_option.widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Intern
        fields = '__all__'
        exclude = ['user','name','location','remote','email','progress','coding','project_management','marketing_skills','web_skills','first_preference', 'second_preference', 'third_preference']
    

class StudentForm3(ModelForm):
    class Meta:
        model = Intern
        fields = '__all__'
        exclude = ['user','name','email','progress','location','remote','coding','project_management','marketing_skills','web_skills','first_preference', 'second_preference', 'third_preference']
    




class ManagerForm(ModelForm):
#name, manager name, job name, job description, day in the life
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['user','progress','location','email','coding','project_management','marketing_skills','web_skills']


    def __init__(self, *args, **kwargs):
        super(ManagerForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget = widgets.TextInput(
            attrs={
                'placeholder': 'Job Name',
                'class': 'form-control',
                'style': 'margin-bottom: 10px'
            })

        self.fields['manager_name'].widget = widgets.TextInput(
            attrs={
                'placeholder': 'Manager Name',
                'class': 'form-control',
                'style': 'margin-bottom: 10px'
            })
    
        self.fields['description'].widget = widgets.Textarea(
            attrs={
                'placeholder': 'Job Description',
                'class': 'form-control',
                'rows':'5',
                'style': 'margin-bottom: 10px'
            })

class ManagerForm2(ModelForm):
#location, remote balance, pay

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['user','progress','name','manager_name','description','email','coding','project_management','marketing_skills','web_skills']

class ManagerForm3(ModelForm):
#skills
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['user','progress','name','manager_name','location','description','email','coding','project_management','marketing_skills','web_skills']
