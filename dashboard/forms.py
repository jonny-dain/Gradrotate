from django.forms import ModelForm
from accounts.models import Job
from users.models import InternPreference

class InternPreferenceForm(ModelForm):


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