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
        exclude = ['name','user','allocation_algorithm','notify_allocations','total_jobs','total_interns','job_creation_date','intern_creation_date','allocation_creation_date','automate_phase']




class AdminForm2(ModelForm):

    job_creation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'style':'color:#6c757d;'}))

    intern_creation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'style':'color:#6c757d;'}))

    allocation_creation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'style':'color:#6c757d;'}))

    automate_phase = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['name','user','allocation_algorithm','phase','notify_allocations','total_jobs','total_interns']

    def __init__(self, *args, **kwargs):
        super(AdminForm2, self).__init__(*args, **kwargs)
        self.fields['automate_phase'].required = False



class AdminToggleAutomaticPhase(ModelForm):

    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['name','user','allocation_algorithm','notify_allocations','total_jobs','total_interns','phase','job_creation_date','intern_creation_date','allocation_creation_date','automate_phase']




class AdminToggleNotify(ModelForm):
    notify_allocations = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'onchange': 'submit();'}))
    
    ALGORITHM =(
        ('Gale Shapely','Gale Shapely'),
        ('Hungarian','Hungarian'),
        ('Pareto','Pareto')

    )

    allocation_algorithm= forms.CharField(label='Allocation Algorithm: ', widget=forms.Select(choices=ALGORITHM))
    allocation_algorithm.widget.attrs.update({'class': 'form-select', 'onchange': 'submit();'})

    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['name','user','total_jobs','total_interns','phase','job_creation_date','intern_creation_date','allocation_creation_date','automate_phase']

    def __init__(self, *args, **kwargs):
        super(AdminToggleNotify, self).__init__(*args, **kwargs)
        self.fields['notify_allocations'].required = False

class AdminToggleAlgorithm(ModelForm):

    ALGORITHM =(
        ('Gale Shapely','Gale Shapely'),
        ('Hungarian','Hungarian'),
        ('Pareto','Pareto')

    )

    allocation_algorithm= forms.CharField(label='Allocation Algorithm: ', widget=forms.Select(choices=ALGORITHM))
    allocation_algorithm.widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['name','user','notify_allocations','total_jobs','total_interns','phase','job_creation_date','intern_creation_date','allocation_creation_date','automate_phase']


