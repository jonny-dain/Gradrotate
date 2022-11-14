from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *


#This function creates job preferences for interns based off skills
def job_preference_dictionary():
    #create a preference dictionary "job": ["intern","intern","intern"]
    
    jobs = Job.objects.all()
    interns = Intern.objects.all()

    jobs_dictionary = {}
    for job in jobs:
        job_dictionary = {}

        for intern in interns:

            skill_difference = abs(job.coding - intern.coding) + abs(job.project_management - intern.project_management) + abs(job.marketing_skills - intern.marketing_skills) + abs(job.web_skills - intern.web_skills)
            # save the skill difference with each of the jobs. if a job has a higher skill difference add to the end 
            #
            job_dictionary[intern] = skill_difference
            #print(" The intern: " + str(intern.name))
            #print(" Skill difference: " + str(skill_difference))
        
        job_dictionary = sorted(job_dictionary.items(), key=lambda x:x[1])
        job_dictionary = dict(job_dictionary)
        intern_list = list(job_dictionary.keys())

        job_dictionary.clear()

        jobs_dictionary[job] = intern_list

    print(jobs_dictionary)
    return jobs_dictionary


#This function creates a dictionary for the interns
def intern_preference_dictionary():
     #create a preference dictionary "intern": ["job","job","job"]

    jobs = Job.objects.all()
    interns = Intern.objects.all()

    interns_dictionary = {}
    for intern in interns:
        intern_dictionary = {}
        preferences = intern.internpreference_set.all()
        for preference in preferences:

            
            intern_dictionary[preference.job] = preference.preference

        intern_dictionary = sorted(intern_dictionary.items(), key=lambda x:x[1])
        intern_dictionary = dict(intern_dictionary)
        job_list = list(intern_dictionary.keys())

        interns_dictionary[intern] = job_list

    print(interns_dictionary)
    return interns_dictionary




   
    

