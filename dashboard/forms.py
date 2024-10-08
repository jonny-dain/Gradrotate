from django.forms import ModelForm
from accounts.models import Job
from users.models import InternPreference
from django import forms

#Preference form for the intern
class InternPreferenceForm(ModelForm):





    class Meta:
        model = InternPreference
        fields = '__all__'
     

    def set_job(self, job):
        data = self.data.copy()
        data['job'] = job
        self.data = data

    def clean(self):
        cleaned_data = self.cleaned_data
        job = cleaned_data.get('job')
        preference = cleaned_data.get('preference')
        
        if (range(preference) == 0):

            self.add_error('preference', 'Event end date should not occur before start date.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preference'].widget.attrs.update({'class': 'form-select'})