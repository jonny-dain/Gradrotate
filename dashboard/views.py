from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Job, Intern
from users.models import InternPreference
from .forms import InternPreferenceForm
from django.forms import inlineformset_factory, BaseFormSet
from django.core.exceptions import ValidationError

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
    jobs = Job.objects.all()
    jobs_count = jobs.count()  

    #only show one form , formset= BaseCheckFormSet
    OrderFormSet = inlineformset_factory(Intern, InternPreference, fields = ('job', 'preference'), extra = jobs_count,max_num=jobs_count)
    intern = request.user.intern
    
    formset = OrderFormSet(instance = intern)
    #form = InternPreferenceForm(initial={'intern': intern})

    #some_formset = formset(initial=[{'id': x} for x in jobs])

    #Zipped the form and jobs
    form_job = zip(formset, jobs)
    form_job2 = zip(formset, jobs)

    #remove the formset context
    context = {'jobs' :jobs, 'jobs_count': range(jobs_count), 'formset': formset, 'zippedlist': form_job,'zippedlist2':form_job2}
    
    #formset.field['job'].initial = jobs[0]

    



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
                print("complete")
                #check if done
                
                intern.progress = 3
                
                intern.save()

                print(intern.progress)
                return HttpResponse("done")
        else:
            
            print('failed')

    return render(request, 'dashboard/dashboard.html', context)
    