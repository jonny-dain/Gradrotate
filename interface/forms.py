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
        exclude = ['name','user','job_creation_date','intern_creation_date','allocation_creation_date','automate_phase']




class AdminForm2(ModelForm):

    job_creation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'style':'color:#6c757d;'}))

    intern_creation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'style':'color:#6c757d;'}))

    allocation_creation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'style':'color:#6c757d;'}))

    automate_phase = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['name','user','phase']

    def __init__(self, *args, **kwargs):
        super(AdminForm2, self).__init__(*args, **kwargs)
        self.fields['automate_phase'].required = False



class AdminToggleAutomaticPhase(ModelForm):

    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['name','user','phase','job_creation_date','intern_creation_date','allocation_creation_date','automate_phase']