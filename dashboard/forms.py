from django.forms import ModelForm
from accounts.models import Job
from users.models import InternPreference
from django import forms

class InternPreferenceForm(ModelForm):



    #PREFS = ((1,1),)
    #jobs = Job.objects.all()
    #for i in range(2,jobs.count()+1):
    #    PREFS = PREFS + ((i,i),)
    
    #pref_option= forms.CharField(label='mp', widget=forms.Select(choices=PREFS))
    #pref_option.widget.attrs.update({'class': 'form-select'})



    class Meta:
        model = InternPreference
        fields = '__all__'
        #fields = ['preference'] yes

    def set_job(self, job):
        data = self.data.copy()
        data['job'] = job
        self.data = data

    def clean(self):
        cleaned_data = self.cleaned_data
        job = cleaned_data.get('job')
        preference = cleaned_data.get('preference')
        print('here')
        if (range(preference) == 0):

            self.add_error('preference', 'Event end date should not occur before start date.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preference'].widget.attrs.update({'class': 'form-select'})