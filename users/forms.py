from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django import forms
from django.forms.widgets import CheckboxSelectMultiple



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
        exclude = ['user','email','progress','computing_skills','computing_skills','analytic_skills','marketing_skills','management_skills','leadership_skills','business_skills','admin_skills','location','remote','coding','project_management','marketing1_skills','web_skills','first_preference', 'second_preference', 'third_preference']
    
        


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
        exclude = ['user','name','location','computing_skills','analytic_skills','marketing_skills','management_skills','leadership_skills','business_skills','admin_skills','remote','email','progress','coding','project_management','marketing1_skills','web_skills','first_preference', 'second_preference', 'third_preference']
    

class StudentForm3(ModelForm):
    class Meta:
        model = Intern
        fields = '__all__'
        exclude = ['user','name','email','progress','location','remote','coding','project_management','marketing1_skills','web_skills','first_preference', 'second_preference', 'third_preference']
    

    def __init__(self, *args, **kwargs):
        super(StudentForm3, self).__init__(*args, **kwargs)


        self.fields["computing_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["computing_skills"].queryset = ComputingSkills.objects.all()
        self.fields['computing_skills'].required = False

        self.fields["analytic_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["analytic_skills"].queryset = AnalyticSkills.objects.all()
        self.fields['analytic_skills'].required = False

        self.fields["marketing_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["marketing_skills"].queryset = MarketingSkills.objects.all()
        self.fields['marketing_skills'].required = False

        self.fields["management_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["management_skills"].queryset = ManagementSkills.objects.all()
        self.fields['management_skills'].required = False

        self.fields["leadership_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["leadership_skills"].queryset = LeadershipSkills.objects.all()
        self.fields['leadership_skills'].required = False

        self.fields["business_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["business_skills"].queryset = BusinessSkills.objects.all()
        self.fields['business_skills'].required = False

        self.fields["admin_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["admin_skills"].queryset = AdminSkills.objects.all()
        self.fields['admin_skills'].required = False




class ManagerForm(ModelForm):
#name, manager name, job name, job description, day in the life
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['user','computing_skills','analytic_skills','marketing_skills','management_skills','leadership_skills','business_skills','admin_skills','progress','location','email','coding','project_management','marketing1_skills','web_skills']


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

class ManagerCreateSkills(forms.Form):
    CATEGORY_CHOICES =  [
        ('Computing', 'Computing'),
        ('Analytic', 'Analytic'),
        ('Marketing', 'Marketing'),
        ('Management', 'Management'),
        ('Leadership', 'Leadership'),
        ('Business', 'Business'),
        ('Admin', 'Admin'),

    ]

    skill_category = forms.CharField(label='What category is the skill?', widget=forms.Select(choices=CATEGORY_CHOICES))
    name = forms.CharField(max_length = 30)
    
    class Meta:
        fields = '__all__'








class ManagerForm2(ModelForm):
#location, remote balance, pay

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['user','computing_skills','analytic_skills','marketing_skills','management_skills','leadership_skills','business_skills','admin_skills','progress','name','manager_name','description','email','coding','project_management','marketing1_skills','web_skills']


class ManagerForm3(ModelForm):
#skills
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['user','progress','name','manager_name','location','description','email','coding','project_management','marketing1_skills','web_skills']

    def __init__(self, *args, **kwargs):
        super(ManagerForm3, self).__init__(*args, **kwargs)


        self.fields["computing_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["computing_skills"].queryset = ComputingSkills.objects.all()
        self.fields['computing_skills'].required = False

        self.fields["analytic_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["analytic_skills"].queryset = AnalyticSkills.objects.all()
        self.fields['analytic_skills'].required = False

        self.fields["marketing_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["marketing_skills"].queryset = MarketingSkills.objects.all()
        self.fields['marketing_skills'].required = False

        self.fields["management_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["management_skills"].queryset = ManagementSkills.objects.all()
        self.fields['management_skills'].required = False

        self.fields["leadership_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["leadership_skills"].queryset = LeadershipSkills.objects.all()
        self.fields['leadership_skills'].required = False

        self.fields["business_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["business_skills"].queryset = BusinessSkills.objects.all()
        self.fields['business_skills'].required = False

        self.fields["admin_skills"].widget = CheckboxSelectMultiple(attrs={'class' : 'btn-check'})
        self.fields["admin_skills"].queryset = AdminSkills.objects.all()
        self.fields['admin_skills'].required = False

