from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Job, Intern
from users.models import InternPreference
from .forms import InternPreferenceForm
from django.forms import inlineformset_factory, BaseFormSet
from django.core.exceptions import ValidationError

def job_skills(jobs):


    job_all_skills =[]
    for job in jobs:

        #take out all the skills and add to a list 
        skills = []
        skills += list(job.computing_skills.all().values_list('name', flat=True))
        skills += list(job.analytic_skills.all().values_list('name', flat=True))
        skills += list(job.marketing_skills.all().values_list('name', flat=True))
        skills += list(job.management_skills.all().values_list('name', flat=True))
        skills += list(job.leadership_skills.all().values_list('name', flat=True))
        skills += list(job.business_skills.all().values_list('name', flat=True))
        skills += list(job.admin_skills.all().values_list('name', flat=True))

        
        #info = {}
        
        #info2 = []

        #for skill in skills:
       #     info = []
            #info.update({skill : (100/len(skills))})
        #    info.append(skill)
        #    info.append(100/len(skills))
        #    info2.append(info)
            

        

        job_all_skills.append(skills)

   
    return job_all_skills



def job_ordered_list(request):
    #create a preference dictionary based on the skill similarities [digital degree, TPO, Change Manager]
    
    jobs = Job.objects.all()
    intern = request.user.intern

    computing_skills_intern = intern.computing_skills.all()
    analytic_skills_intern = intern.analytic_skills.all()
    marketing_skills_intern = intern.marketing_skills.all()
    management_skills_intern = intern.management_skills.all()
    leadership_skills_intern = intern.leadership_skills.all()
    business_skills_intern = intern.business_skills.all()
    admin_skills_intern = intern.admin_skills.all()


    jobs_dictionary = {}
    job_dictionary = {}
    for job in jobs:
        similarity_weighting = 0
        
        computing_skills_job = job.computing_skills.all()
        analytic_skills_job = job.analytic_skills.all()
        marketing_skills_job = job.marketing_skills.all()
        management_skills_job = job.management_skills.all()
        leadership_skills_job = job.leadership_skills.all()
        business_skills_job = job.business_skills.all()
        admin_skills_job = job.admin_skills.all()

        similarity_weighting = len(list(set(computing_skills_job).intersection(computing_skills_intern)))
        similarity_weighting += len(list(set(analytic_skills_job).intersection(analytic_skills_intern)))
        similarity_weighting += len(list(set(marketing_skills_job).intersection(marketing_skills_intern)))
        similarity_weighting += len(list(set(management_skills_job).intersection(management_skills_intern)))
        similarity_weighting += len(list(set(leadership_skills_job).intersection(leadership_skills_intern)))
        similarity_weighting += len(list(set(business_skills_job).intersection(business_skills_intern)))
        similarity_weighting += len(list(set(admin_skills_job).intersection(admin_skills_intern)))

        #This calculates the weighting...


       #If the locations are the same add one to the weighting - total max is now 6
        if job.location == intern.location:
            similarity_weighting += 1

        #If remote is the same add one to the weighting - total max is now 7
        if job.remote == intern.remote:
            similarity_weighting += 1

        #Section for preferred wage

        similarity_weighting = round(similarity_weighting/7 * 100)

        job_dictionary[job] = similarity_weighting


    
    job_dictionary = sorted(job_dictionary.items(), key=lambda x:x[1], reverse=True)

    job_dictionary = dict(job_dictionary)
    

    return job_dictionary
