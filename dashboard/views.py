from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Job, Intern
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












#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Intern'])
def preference(request):
    #jobs = Job.objects.all()
    job_with_percentage = job_ordered_list(request)

    jobs_percentage = list(job_with_percentage.values())
    jobs = list(job_with_percentage.keys())

    jobs_count = len(jobs)

    counter = 0
    for job in jobs:
        counter += 1
        if not InternPreference.objects.filter(intern = request.user.intern, job = job).exists():
            InternPreference.objects.create(intern = request.user.intern, job = job, preference = counter)


    #HAS TO CHANGE
    intern_preferences = InternPreference.objects.filter(intern = request.user.intern)
    
    #Can be placed in function
    
    intern_preference_dictionary = {}
    for intern_preference in intern_preferences:
        
        intern_preference_dictionary[intern_preference] = intern_preference.preference

    intern_preference_dictionary = dict(sorted(intern_preference_dictionary.items(), key=lambda x:x[1]))


    intern_preferences = list(intern_preference_dictionary.keys())
    

    #sort based on preferences..








    OrderFormSet = inlineformset_factory(Intern, InternPreference, fields = ('job', 'preference'), extra = jobs_count,max_num=jobs_count)
    intern = request.user.intern
    
    formset = OrderFormSet(instance = intern)




    
    #This gets all the skills for each of the jobs and gives a %
    all_job_skills = job_skills(jobs = jobs)

   

    #Zipped the form and jobs
    form_job = zip(formset, jobs)


    form_job2 = zip(jobs, all_job_skills, jobs_percentage)
    
    print('here')

    #remove the formset context
    #context = { 'jobs_count': range(jobs_count), 'formset': formset, 'zippedlist': form_job,'zippedlist2':form_job2}
    context = { 'jobs_count': range(jobs_count), 'formset': formset, 'intern_preferences': intern_preferences,'zippedlist2':form_job2}
    return render(request, 'dashboard/dashboard.html', context)








    if request.method == 'POST':
        #form = InternPreferenceForm(request.POST)
        formset = OrderFormSet(request.POST, instance = intern)

        counter = 0
        
        for form in formset:
            form.job = jobs[counter]
            #form.set_job(jobs[counter])
            counter = counter + 1
        
        
        if formset.is_valid():
            #Validation of form
            jobs_list = []
            preference_list = []
            errors_list = []

            counter = 0

            for form in formset:
            
                
                #form.cleaned_data['job'] = jobs[counter]
                #job = form.cleaned_data.get('job')
                preference_number = form.cleaned_data.get('preference')
                #print(form.job)
                #print(preference_number)
                #form.set_job(jobs[counter])
                counter = counter + 1


                #Set job to counter form.job = jobs.get[loop_counter].. then the loop has to contain the job name
                #zip form with list of jobs https://stackoverflow.com/questions/12684128/looping-through-two-objects-in-a-django-template
                

                #if job in jobs_list:
                    #errors_list.append('All jobs must have a preference')
                    
                if preference_number in preference_list:
                    errors_list.append('All jobs must have different preferences')
                    
                #jobs_list.append(job)
                preference_list.append(preference_number)
            if len(errors_list) > 0:
                
                context = {'jobs' :jobs, 'jobs_count': range(jobs_count), 'formset': formset, 'errorlist':errors_list, 'zippedlist': form_job}
                return render(request, 'dashboard/dashboard.html', context)
            else:
                #formset doesn't save job
                counter = 0
                for form in formset:
                    preference_number = form.cleaned_data.get('preference')
                    
                    

                    #this might have fixed it....

                    obj = form.save(commit=False)
                    obj.job = jobs[counter]
                    obj.save()
                    counter = counter + 1

                    
                    
                    #FORM.preference doesnt exist?!?


                    #print(form.preference)
                #formset.save()

                #check if done
                
                intern.progress = 3
                
                intern.save()


                return HttpResponse("done")
        else:
            
            print('failed')

    return render(request, 'dashboard/dashboard.html', context)
    









def sort(request):
    preference_pks_order = request.POST.getlist('preference_order')
    intern_preferences = []

    for idx, preference_pk in enumerate(preference_pks_order, start=1):
        intern_preference = InternPreference.objects.get(pk = preference_pk)
        intern_preference.preference = idx
        intern_preference.save()
        intern_preferences.append(intern_preference)



    #return redirect('../../dashboard')
    context = {'intern_preferences': intern_preferences}
    
    #return redirect('../../../dashboard')

    return render(request, 'dashboard/dashboard-pref.html', context)