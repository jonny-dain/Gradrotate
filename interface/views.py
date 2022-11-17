from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
from interface.preferences import *
from users.models import *
from collections import deque

# Create your views here.

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def admin_interface(request):
    
    jobs = Job.objects.all()
    interns = Intern.objects.all()

    intern_preference = intern_preference_dictionary()
    job_preference = job_preference_dictionary()
    
    job_set = set(jobs)
    intern_set = set(interns)
    #print(job_set)
    #print(intern_set)

    #print(str(intern_preference))
    #print(str(job_preference))
    #print(" ")

    #Want to create a function that takes in interns, jobs, job preferences, intern preferences and formulates pairs?

    context = {'jobs' :jobs , 'interns' : interns}
    return render(request, 'interface/interface.html', context)

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def intern_interface(request):
    
    
    interns = Intern.objects.all()
    jobs = Job.objects.all()

    intern_preference = intern_preference_dictionary()

    context = {'interns' : interns, 'jobs' :jobs , 'intern_preference' : intern_preference}
    return render(request, 'interface/interns.html', context)

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def job_interface(request):
    
    jobs = Job.objects.all()
    interns = Intern.objects.all()

    job_preference = job_preference_dictionary()

    context = {'jobs' :jobs , 'interns' : interns, 'job_preference' : job_preference}
    return render(request, 'interface/jobs.html', context)




#This is to delete Interns from the system
#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteIntern(request, pk):

    
    intern = Intern.objects.get(id=pk)
    InternPreference.objects.filter(intern = intern).delete()
    User.objects.get(intern = intern).delete()
    intern.delete()
    #need to delete all interns items
    return redirect('../../../admin_interface/interns/')

def deleteJob(request, pk):

    job = Job.objects.get(id=pk)
    InternPreference.objects.filter(job = job).delete()
    User.objects.get(job = job).delete()
    job.delete()
    return redirect('../../../admin_interface/jobs/')








