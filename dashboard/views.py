from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Job, Intern
from accounts.permissions import allowed_users, required_phase, update_progress
from dashboard.dashboard_info import *
from users.models import InternPreference
from .forms import InternPreferenceForm
from django.forms import inlineformset_factory, BaseFormSet
from django.core.exceptions import ValidationError
import json

# Create your views here.

#Validates the form
class BaseCheckFormSet(BaseFormSet):
    def clean(self):
         """Checks that no preferences are the same"""
         if any(self.errors):
             return
         jobs = []
         for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
            job = form.cleaned_data.get('job')
            if job in jobs:
                raise ValidationError("Articles in a set must have distinct titles.")
            jobs.append(job)




# Creates preferences
@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Intern'])
@update_progress(4)
@required_phase(phase=['Intern collection'])
def preference(request):
    #creates list for new interns based on skills before
    job_with_percentage = job_ordered_list(request)

    jobs = list(job_with_percentage.keys())

    counter = 0
    for job in jobs:
        


        counter += 1
        if not InternPreference.objects.filter(intern = request.user.intern, job = job).exists():
            InternPreference.objects.create(intern = request.user.intern, job = job, preference = counter)
    
    #orders list based on the prefence list
    job_with_percentage = job_ordered_preference_list(request)

    #Gathers information on the jobs - the percentage of each job, total jobs and jobs count
    jobs_percentage = list(job_with_percentage.values())
    jobs = list(job_with_percentage.keys())
    jobs_count = len(jobs)


    #gets all the intern job preferences in a dictionary
    intern_preferences = get_intern_preferences(request)
    

    #This gets all the skills for each of the jobs and gives a %
    all_job_skills = job_skills(jobs = jobs)

    #Zipped the form and jobs
    form_job = zip(jobs, all_job_skills, jobs_percentage)

    context = { 'jobs_count': range(jobs_count), 'intern_preferences': intern_preferences,'zippedlist2':form_job}
    return render(request, 'dashboard/dashboard.html', context)




#Sorts the jobs based on preferences
@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Intern'])
def sort(request):
    preference_pks_order = request.POST.getlist('preference_order')
    intern_preferences = []

    for idx, preference_pk in enumerate(preference_pks_order, start=1):
        intern_preference = InternPreference.objects.get(pk = preference_pk)
        intern_preference.preference = idx
        intern_preference.save()
        intern_preferences.append(intern_preference)


    job_with_percentage = job_ordered_preference_list(request)

    jobs_percentage = list(job_with_percentage.values())
    jobs = list(job_with_percentage.keys())
    jobs_count = len(jobs)

    all_job_skills = job_skills(jobs = jobs)
    form_job2 = zip(jobs, all_job_skills, jobs_percentage)
    
    context = { 'jobs_count': range(jobs_count), 'intern_preferences': intern_preferences,'zippedlist2':form_job2}

    return render(request, 'dashboard/dashboard-pref.html', context)